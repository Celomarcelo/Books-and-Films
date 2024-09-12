from rest_framework import serializers
from .models import Review, Profile
from django.contrib.auth.models import User


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile_image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'profile_image']

    def get_profile_image(self, user):
        profile = Profile.objects.get(user=user)
        request = self.context.get('request')
        if profile.image:
            image_url = profile.image.url
            return request.build_absolute_uri(image_url)
        return None
