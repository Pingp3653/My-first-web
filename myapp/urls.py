from .views import *
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',home,name="home-page"),
    path('contact/',contact,name="contact-page"),
    path('about/',about,name="about-page"),
    path('register',Regidter,name='register'),
    path('login',Login,name='login'),
]


