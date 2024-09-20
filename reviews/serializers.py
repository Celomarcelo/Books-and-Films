from rest_framework import serializers
from .models import Review, Profile
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']


class UserSerializer(serializers.ModelSerializer):
    profile_image = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'profile']

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
            profile.save()

        return instance
