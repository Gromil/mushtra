from rest_framework import serializers

from common.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')
    first_name = serializers.CharField(source='user.first_name')

    class Meta:
        model = Profile
        fields = '__all__'
