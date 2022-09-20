# 当前应用的 URL 配置

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]