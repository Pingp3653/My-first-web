from .views import *
from django.urls import path

urlpatterns = [
    path('',home,name="home-page"),
    path('contact/',contact,name="contact-page"),
    path('about/',about,name="about-page"),

    path('register',Regidter,name='register'),
    path('login',Login,name='login'),
]


