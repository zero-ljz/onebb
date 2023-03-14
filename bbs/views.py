from django.shortcuts import render, redirect, resolve_url, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag
from accounts.models import User
from .forms import RegisterForm, LoginForm, PostCreateForm, CommentCreateForm

from django.utils import timezone
from django.views import View
from django.urls import reverse, resolve, reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as dUser

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def index(request):
    archives = Post.objects.raw("SELECT post.id, CAST(STRFTIME('%m', post.created) AS INTEGER) AS month, CAST(STRFTIME('%Y', post.created) AS INTEGER) AS year, count(*) AS count FROM post GROUP BY year, month ORDER BY post.created DESC LIMIT 12 OFFSET -1")[:5]
    top_posts = Post.objects.order_by('-read_count')[:5]
    new_comments = Comment.objects.order_by('-created')[:5]
    return render(request, 'bbs/index.html', { 'archives': archives, 'top_posts': top_posts, 'new_comments':new_comments})


# class LoginView(View):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, 'bbs/login.html', {'form': form})
#     def post(self, request):
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect(reverse('accounts:user-detail', args=[user.id])) # HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#         else:
#             return HttpResponse('登录失败')


# class RegisterView(View):
#     def get(self, request):
#         form = RegisterForm()
#         context = {'form': form}
#         return render(request, 'bbs/register.html', context)
#     def post(self, request):
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         User.objects.create(username=username, password=password)
#         return HttpResponse('注册成功')
    

# class LogoutView(View):
#     def get(self, request):
#         logout(request)
#         return redirect(reverse('bbs:index'))


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    # queryset = Post.objects.all() # 赋值 model 或 queryset 二选一
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
        context['object_list'] = get_list_or_404(Post, tags__name__contains=name)
        return context


class PostDetailView(DetailView):
    queryset = Post.objects.all() # 指定对象列表
    # context_object_name = '' # 制作"友好"的模板上下文

    def post(self, request, *args, **kwargs):

        form = CommentCreateForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user # 当前登录用户
            post_id = self.kwargs['pk']
            obj.post = get_object_or_404(Post, id=post_id)
            obj.save()
            return redirect(reverse('bbs:post-detail', args=[post_id]))
        else:
            return HttpResponse('评论失败')






    '''
    def get(self, request, *args, **kwargs):
        last_book = self.get_queryset().latest('publication_date')
        response = HttpResponse(
            # RFC 1123 date format.
            headers={'Last-Modified': last_book.publication_date.strftime('%a, %d %b %Y %H:%M:%S GMT')},
        )
        return response
    
    def get_queryset(self): # 通过URL中的某个键来过滤列表页面里的对象
        self.publisher = get_object_or_404(Publisher, name=self.kwargs['publisher'])
        return Book.objects.filter(publisher=self.publisher)
    '''

    def get_object(self): # 在调用通用视图前后执行一些附加任务
        obj = super().get_object()
        # 递增阅读次数
        obj.read_count += 1
        obj.save()
        return obj
       
    def get_context_data(self, **kwargs): # 添加额外的上下文
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        # Add in a QuerySet of all the comments
        context['comment_list'] = Comment.objects.filter(post_id=pk, reviewed=1)
        context['like_list'] = Like.objects.filter(liked_id=pk)
        context['collect_list'] = Collect.objects.filter(collected_id=pk)
        form = CommentCreateForm()
        context['form'] = form

        return context

class LikeView(View):
    def get(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        try:
            obj = Like.objects.get(liked_id=post_id, liker_id=request.user.pk)
        except Like.DoesNotExist:
            like = Like(liked_id=post_id, liker_id=request.user.pk)
            like.save() # 点赞文章
        else:
            obj.delete() # 取消点赞
        return redirect(reverse('bbs:post-detail',args=[post_id]))
    
class CollectView(View):
    def get(self, request, *args, **kwargs):
        post_id = self.kwargs['post_id']
        try:
            obj = Collect.objects.get(collected_id=post_id, collector_id=request.user.pk)
        except Collect.DoesNotExist:
            collect = Collect(collected_id=post_id, collector_id=request.user.pk)
            collect.save() # 收藏文章
        else:
            obj.delete() # 取消收藏
        return redirect(reverse('bbs:post-detail',args=[post_id]))

class MessageCreateView(CreateView):
    model = Message
    fields = ['content']
    success_url = '/accounts/users/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.sender = get_object_or_404(User, username=self.request.user.username) # 发件人 指定为当前登录用户
        self.object.received = get_object_or_404(User, pk=self.kwargs['user_id'])
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class FollowView(View):
    def get(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        try:
            obj = Follow.objects.get(followed_id=user_id, follower_id=request.user.pk)
        except Follow.DoesNotExist:
            follow = Follow(followed_id=user_id, follower_id=request.user.pk)
            follow.save() # 关注用户
        else:
            obj.delete() # 取消关注
        return redirect(reverse('accounts:user-detail',args=[user_id]))

class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    #exclude = ['is_active','is_staff','is_superuser']
    template_name_suffix = '_update_form'
    success_url = '/accounts/users'


class PostCreateView(CreateView):
    template_name = 'bbs/post_form.html'
    form_class = PostCreateForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = get_object_or_404(User, username=self.request.user.username) # 指定为当前登录用户
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


    def get_initial(self, *args, **kwargs):
        initial = super(PostCreateView, self).get_initial(**kwargs)
        initial['content'] = '说点什么吧'
        return initial


    def get_object(self): # 在调用通用视图前后执行一些附加任务
        obj = super().get_object()
        # Record the last accessed date
        obj.author = get_object_or_404(User, username='yk')
        self.object['author'] = get_object_or_404(User, username='yk')
        obj.save()
        return obj
    
    def get_context_data(self, **kwargs): # 添加额外的上下文
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #pk = self.kwargs['pk']
        #self.object.
        return context





class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content','content_html','tags']
    template_name_suffix = '_update_form'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('bbs:post-list')


class CommentCreateView(CreateView):
    model = Comment
    fields = ['content']
    success_url = '/bbs/posts/'
    template_name = 'bbs/post_detail.html'
    template_name_suffix = ''
    #context_object_name = 'form1'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = get_object_or_404(User, username=self.request.user.username) # 发布者 指定为当前登录用户

        post_id = self.kwargs['post_id']
        post = Post.objects.filter(id=post_id)[0] # 评论的文章
        self.object.post = post
        self.object.reviewed = True

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

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

