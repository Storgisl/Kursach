from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    url = models.URLField()
    preview = models.ImageField(default='default_courses.jpg', upload_to="course_preview")
    tag = models.CharField(max_length=100)