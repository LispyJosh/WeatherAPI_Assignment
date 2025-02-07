from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Profile Model with Resizing
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile_pics/', 
        default='default_profile_pic.png',  # Default profile picture
        blank=True, 
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_pic:
            try:
                img = Image.open(self.profile_pic.path)
                if img.height > 300 or img.width > 300:  # Max dimensions for profile pictures
                    output_size = (300, 300)
                    img.thumbnail(output_size)
                    img.save(self.profile_pic.path)
            except Exception as e:
                print(f"Error resizing profile picture: {e}")

    def __str__(self):
        return self.user.username