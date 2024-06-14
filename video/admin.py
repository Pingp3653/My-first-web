from django.contrib import admin
from .models import Youtube
from django_summernote.admin import SummernoteModelAdmin



class YoutubeAdmin(admin.ModelAdmin):
    list_display = ['id','title','description']
    list_editable = ['title']


admin.site.register(Youtube,YoutubeAdmin)
