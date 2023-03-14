# 当前应用的 URL 配置

from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='index'),
    #path('', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(redirect_field_name='next', extra_context={},redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),


    path('register/', views.RegisterView.as_view(), name='register'),

    path('u/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    path('users/', views.UserListView.as_view(), name='user-list'),

    path('profile/<int:pk>/', views.UserUpdateView.as_view(), name='user-update'),




]