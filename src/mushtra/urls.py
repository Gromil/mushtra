from django.urls import path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from mushtra.views import TaskViewSet, ResultViewSet

router = DefaultRouter()

router.register(prefix='tasks', viewset=TaskViewSet)
router.register(prefix='results', viewset=ResultViewSet)


urlpatterns = router.urls

urlpatterns += (
    path('auth/', views.obtain_auth_token),
)
