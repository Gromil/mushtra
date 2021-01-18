from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from common.views import ProfileViewSet

router = DefaultRouter()

router.register(prefix='profiles', viewset=ProfileViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('auth/', views.obtain_auth_token)
]
