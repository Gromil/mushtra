from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from common.models import Profile
from common.serializers import ProfileSerializer


class ProfFilter(filters.FilterSet):
    age = filters.NumberFilter(field_name="age", lookup_expr='gte')

    class Meta:
        model = Profile
        fields = ('name', 'nick', 'age')


class ProfileViewSet(ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = (DjangoFilterBackend,)
    # search_fields = ('name', 'nick')
    filterset_class = ProfFilter
