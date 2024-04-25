from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    date = models.DateField(default=timezone.now)
    text = models.TextField()
    tag = models.CharField(max_length=100, default='')
    preview = models.ImageField(default="default_article.jpg", upload_to='articles_preview')

    class Meta:
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title
    
    def save(self,  *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.preview.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.preview.path)