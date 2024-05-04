from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()
    preview = models.ImageField(default="default_video.jpg", upload_to='videos_preview')
        