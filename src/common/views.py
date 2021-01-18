from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from common.models import Profile
from common.serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user__username'
