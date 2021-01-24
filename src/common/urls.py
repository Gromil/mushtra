from rest_framework.routers import DefaultRouter

from common.views import ProfileViewSet

router = DefaultRouter()

router.register(prefix='profiles', viewset=ProfileViewSet)

urlpatterns = router.urls
