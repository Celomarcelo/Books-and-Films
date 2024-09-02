from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_director', 'genre', 'rating', 'created_at', 'user')
    search_fields = ('title', 'author_director', 'genre')
