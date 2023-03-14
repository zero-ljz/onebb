from django.shortcuts import render, redirect, resolve_url, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password
from django.urls import reverse, resolve, reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from .forms import CustomUserCreationForm

#from .models import User
from bbs.models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.



def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/register.html"



class UserListView(ListView):
    model = User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    # 未登录时跳转信息
    login_url = '/accounts/login/'
    redirect_field_name = 'next' # redirect_to

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #username = self.kwargs['username']
        #user = get_object_or_404(User, username=username)
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
    

class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password','email','name','url']
    template_name_suffix = '_update_form'









# class RegisterView(CreateView):
#     model = User
#     fields = ['username','name','password','email']
#     success_url = '/accounts/login/'
#     template_name = 'registration/register.html'

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.password = make_password(self.object.password)
#         self.object.save()
#         return HttpResponseRedirect(self.get_success_url())

# def register(request):  
#     if request.method == 'POST':  
#         form = UserCreationForm(request.POST)  
#         if form.is_valid():  
#             form.save()  
#             messages.success(request, 'Account created successfully') 
#     else:  
#         form = UserCreationForm()  
#         context = {  
#             'form':form  
#         }  
#         return render(request, 'registration/register.html', context)  