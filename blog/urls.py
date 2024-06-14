from django.urls import path
from .views import *
urlpatterns = [
    path('',all_post,name="post-page"),
    path('detail/<slug:slug>/',post_detail,name="post-detail-page")
]
