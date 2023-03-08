# 当前应用的 URL 配置

from django.urls import path

from . import views

app_name = 'bbs'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('archive/<int:year>/<int:month>/', views.ArchivePostListView.as_view(), name='archive-detail'),
    path('tag/<str:name>/', views.TagPostListView.as_view(), name='tag-detail'),

    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('new_post/', views.PostCreateView.as_view(), name='post-create'),
    path('edit_post/<int:pk>/', views.PostUpdateView.as_view(), name='post-update'),
    path('delete_post/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),

    path('comment/create/<int:post_id>/<int:comment_id>/', views.CommentCreateView.as_view(), name='comment-create'),

    path('new_message/<int:user_id>/', views.MessageCreateView.as_view(), name='message-create'),
    
    path('tags/', views.TagListView.as_view(), name='tag-list'),

    path('users/', views.UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]