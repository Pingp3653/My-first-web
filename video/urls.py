from django.urls import path
from .views import *
urlpatterns = [
    path("", all_youtube_video, name='all-youtube-page'),
    path("video/<slug:slug>", detail_youtube_video, name='detail-youtube-page'),
]