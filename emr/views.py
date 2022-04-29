from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Team, EMR, EnvironmentInstance, Environment
from .serializers import TeamSerializer, EnvironmentSerializer, EnvironmentInstanceSerializer, EMRSerializer


# Create your views here.

# TODO Define ViewSet for CRUD Operations

class TeamViewSet(GenericViewSet, ListModelMixin):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class EnvironmentViewSet(GenericViewSet, ListModelMixin):
    queryset = Environment.objects.all()
    serializer_class = EnvironmentSerializer


class EnvironmentInstanceViewSet(GenericViewSet, ListModelMixin):
    queryset = EnvironmentInstance.objects.all()
    serializer_class = EnvironmentInstanceSerializer


class EMRViewSet(GenericViewSet, ListModelMixin):
    queryset = EMR.objects.all()
    serializer_class = EMRSerializer
