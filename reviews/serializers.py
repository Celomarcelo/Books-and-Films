from rest_framework import serializers
from .models import Review, Profile, Genre, Category, Like, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(
        source='profile.image', allow_null=True, required=False)
    biography = serializers.CharField(
        source='profile.biography', allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'profile_image', 'biography', 'id']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile', None)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        if profile_data:
            profile, created = Profile.objects.get_or_create(user=instance)
            profile.image = profile_data.get('image', profile.image)
            profile.biography = profile_data.get(
                'biography', profile.biography)
            profile.save()

        return instance


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name',]


class CategorySerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'genres']

class ProfileSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(
        source='profile.image', allow_null=True, required=False)
    biography = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['profile_image', 'biography']


class UserFavoriteSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(
        source='profile.image', allow_null=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'profile', 'profile_image']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user', 'review', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField(source='user.username')
    user_id = serializers.ReadOnlyField(source='user.id')

    class Meta:
        model = Comment
        fields = ['id', 'user_id', 'user_name', 'review', 'content', 'created_at']

class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    genre_name = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'title', 'author_director', 'genre', 'genre_name',
                  'rating', 'content', 'img', 'created_at', 'user', 'comments' ]

    def get_genre_name(self, obj):
        return obj.genre.name
    
    def create(self, validated_data):
        user = self.context['request'].user
        validated_data.pop('user', None)
        review = Review.objects.create(user=user, **validated_data)
        return review


