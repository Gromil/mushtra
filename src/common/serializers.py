from django.contrib.auth.models import User
from rest_framework import serializers

from common.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    password = serializers.CharField(source='user.password', write_only=True)

    def create(self, validated_data):
        username = validated_data['user']['username']
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('username already exists')
        user = User.objects.create(**validated_data['user'])
        profile = Profile.objects.create(user=user)
        return profile

    class Meta:
        model = Profile
        fields = (
            'username', 'first_name', 'password', 'active', 'telegram_fio',
            'telegram_username', 'created_at'
        )
