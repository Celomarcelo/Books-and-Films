from django.contrib.auth.models import User
from django.db import models


class Review(models.Model):
    title = models.CharField(max_length=255)
    author_director = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    img = models.ImageField(upload_to='reviews/', null=True, blank=True)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')

    def __str__(self):
        return self.user.username