from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
# Create your models here.

#username, email, password, date_registred, profile avatar, history of articles

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='', unique=True)
    # Remove password field, as it's already handled by the User model
    birthday = models.DateField(null=True, blank=True, default=timezone.now)
    image = models.ImageField(default='default_profile.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # Override the save method of the model
    def save(self,  *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path) # Open image

        # resize image
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size) # Resize image
            img.save(self.image.path) # Save it again and override the larger image