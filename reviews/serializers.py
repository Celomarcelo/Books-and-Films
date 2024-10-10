from rest_framework import serializers
from .models import Review, Profile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.ImageField(source='profile.image')
    biography = serializers.CharField(
        source='profile.biography', allow_blank=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'profile_image', 'biography']

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


class ReviewSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'title', 'author_director', 'genre',
                  'rating', 'content', 'img', 'created_at', 'user']


class ProfileSerializer(serializers.ModelSerializer):
    biography = serializers.CharField(required=False)

    class Meta:
        model = Profile
        fields = ['image', 'biography']
