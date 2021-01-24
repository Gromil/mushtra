from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path(route='api/', view=include(arg='common.urls')),
    path(route='api/', view=include(arg='mushtra.urls')),
    path(route='admin/', view=admin.site.urls)
)
