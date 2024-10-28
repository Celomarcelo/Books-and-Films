from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, related_name='genres', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=255)
    author_director = models.CharField(max_length=255)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
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
    favorites = models.ManyToManyField(User, related_name='favorited_by', blank=True)
    image = models.ImageField(
        upload_to='profile_images/', default='default.jpg')
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
    
    
class Like(models.Model):
    review = models.ForeignKey(Review, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('review', 'user')

class Comment(models.Model):
    review = models.ForeignKey(Review, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

