from django.contrib import admin
from django.urls import path, re_path
from . import views



urlpatterns = [
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
]