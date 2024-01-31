from django.contrib import admin
from .models import Movie, VideoFile

# Register your models here.
admin.site.register(Movie)
admin.site.register(VideoFile)