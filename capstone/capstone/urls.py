from datetime import datetime
from django.urls import re_path, path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls),
    re_path(r'^$',views.index,name='index'),
    re_path(r'^special/',views.special,name='special'),
    re_path('', include('app.urls', namespace='app')),
    re_path(r'^logout/$', views.user_logout, name='logout'),
    path('foodie/', views.foodie, name='foodie'),
    path(r'yelping/', views.yelping, name='yelping'),
    path(r'home/yelping/', views.yelping, name='yelping'),
    path('googling/', views.googling, name='googling'),
    path('nutritioning/', views.nutritioning, name='nutritioning'),
    path('foodmacros/', views.foodmacros, name='foodmacros')

]
