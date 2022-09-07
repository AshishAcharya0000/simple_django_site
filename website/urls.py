from django.contrib import admin
from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    #
    path('', views.home, name='homepage'),
    path('about_us/', views.aboutus, name='aboutus'),
    path('more/', views.more, name='more'),
]