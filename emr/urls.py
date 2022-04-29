
from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import TeamViewSet, EMRViewSet, EnvironmentViewSet, EnvironmentInstanceViewSet


router = SimpleRouter()
router.register('teams', TeamViewSet, basename='teams')
router.register('environments', EnvironmentViewSet, basename='teams')
router.register('environment-instances', EnvironmentInstanceViewSet, basename='teams')
router.register('emr', EMRViewSet, basename='teams')

urlpatterns = [
    path('', include((router.urls, 'emr'), namespace='api')),
]
