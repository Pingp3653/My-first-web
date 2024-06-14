from django.shortcuts import render,get_object_or_404
from .models import *

def all_youtube_video(request):
    all_video = Youtube.objects.all().order_by('id').reverse()[:9]

    context = {"all_video": all_video}

    return render(request, 'myapp/all-youtube.html', context)

def detail_youtube_video(request, slug):
    detail_video = get_object_or_404(Youtube, slug=slug)
    all_detail_video = Youtube.objects.all().order_by('date_created').reverse()[:6]

    context = {"detail_video": detail_video, "all_detail_video": all_detail_video}

    return render(request, 'myapp/detail-youtube.html', context)
