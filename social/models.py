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

# Post Model with Resizing and Optional Image
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='posts/', 
        blank=True,  # Allow posts without an image
        null=True  # Allow posts without an image
    )
    caption = models.TextField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            try:
                img = Image.open(self.image.path)
                if img.height > 1080 or img.width > 1080:  # Max dimensions for posts
                    output_size = (1080, 1080)
                    img.thumbnail(output_size)
                    img.save(self.image.path)
            except Exception as e:
                print(f"Error resizing post image: {e}")

    def __str__(self):
        return f"Post by {self.user.username} at {self.created_at}"

# Message Model
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} to {self.recipient.username} at {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']  # Ensures messages are ordered by the most recent by default

# Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on post {self.post.id}"
