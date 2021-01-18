from django.contrib.auth.models import User
from rest_framework import serializers

from common.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')
    password = serializers.CharField(source='user.password', write_only=True)

    def create(self, validated_data):
        user = User.objects.create(**validated_data['user'])
        profile = Profile.objects.create(user=user)
        return profile

    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'password', 'active')
