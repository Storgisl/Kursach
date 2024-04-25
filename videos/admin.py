from atexit import register
from django.contrib import admin
from .models import Video
# Register your models here.
@admin.register(Video)
class Video(admin.ModelAdmin):
    pass