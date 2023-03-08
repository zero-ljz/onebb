from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse, Http404

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag, User
from .forms import RegisterForm, LoginForm

from django.utils import timezone
from django.views import View
from django.urls import reverse, resolve, reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as dUser

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    archives = Post.objects.raw("SELECT post.id, CAST(STRFTIME('%m', post.created) AS INTEGER) AS month, CAST(STRFTIME('%Y', post.created) AS INTEGER) AS year, count(*) AS count FROM post GROUP BY year, month ORDER BY post.created DESC LIMIT 12 OFFSET -1")
    top_posts = Post.objects.raw("SELECT * FROM post ORDER BY read_count DESC")
    new_comments = Comment.objects.raw("SELECT * FROM comment ORDER BY created DESC")
    return render(request, 'bbs/index.html', { 'archives': archives, 'top_posts': top_posts, 'new_comments':new_comments})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'bbs/login.html', {'form': form})
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('bbs:user-detail', args=[user.id]))
        else:
            return HttpResponse('登录失败')


class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'bbs/register.html', context)
    def post(self, request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        dUser.objects.create(username=username, password=password)
        return HttpResponse('注册成功')
    

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('bbs:index'))


class PostListView(ListView):
    model = Post
    # context_object_name = ''
    # queryset = Post.objects.all()
    # template_name = ''

class ArchivePostListView(PostListView):    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        year = self.kwargs['year']
        month = self.kwargs['month']

        # Add in a QuerySet of all the posts
        context['object_list'] = Post.objects.filter(created__year=year, created__month=month)
        # SELECT * FROM post WHERE CAST(STRFTIME('%Y', post.created) AS INTEGER) = 2022 AND CAST(STRFTIME('%m', post.created) AS INTEGER) = 3
        return context
    
class TagPostListView(PostListView):    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        name = self.kwargs['name']

        # Add in a QuerySet of all the posts
        context['object_list'] = Post.objects.filter(tags__name__contains=name)
        return context


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # Add in a QuerySet of all the comments
        context['comment_list'] = Comment.objects.filter(post_id=pk, reviewed=1)
        return context

class MessageCreateView(CreateView):
    model = Message
    fields = ['content','received','sender']
    success_url = '/bbs/users/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs['user_id']
        user = User.objects.filter(id=user_id)[0]
        context['user'] = user # 接收消息的用户
        return context

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content','content_html','author','tags']
    success_url = '/bbs/posts/'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content','content_html','author','tags']
    success_url = '/bbs/posts/'
    template_name_suffix = '_update_form'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('bbs:post-list')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content','reviewed','author','post']
    success_url = '/bbs/posts/'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        post_id = self.kwargs['post_id']
        comment_id = self.kwargs['comment_id']

        post = Post.objects.filter(id=post_id)[0] # 评论的文章
        comment = Comment.objects.filter(id=comment_id)[0] if comment_id != 0 else {'content': '无'} # 回复的评论

        # Add in a QuerySet of all the comments
        context['post'] = post
        context['comment'] = comment
        return context

class TagListView(ListView):
    model = Tag


class UserListView(ListView):
    model = User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    # 未登录时跳转信息
    login_url = '/bbs/login/'
    redirect_field_name = 'next' # redirect_to

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # Add in a QuerySet of all the comments
        context['post_list'] = Post.objects.filter(author__id=pk)
        context['follow_list'] = User.objects.filter(followed_user__follower_id=pk)
        context['fans_list'] = User.objects.filter(follower_user__followed_id=pk)
        context['message_list'] = Message.objects.filter(received_id=pk)
        context['collect_list'] = Post.objects.filter(collect__collector_id=pk)
        context['like_list'] = Post.objects.filter(like__liker_id=pk)
        context['comment_list'] = Comment.objects.filter(author_id=pk, reviewed=1)
        context['notification_list'] = Notification.objects.filter(receiver_id=pk)
        context['log_list'] = Log.objects.filter(owner_id=pk)
        

        return context