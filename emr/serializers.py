from rest_framework import serializers

from .models import Team, Environment, EnvironmentInstance, EMR


# TODO Define Serializers

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'


class EMRSerializer(serializers.ModelSerializer):
    class Meta:
        model = Environment
        fields = '__all__'


class EnvironmentInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnvironmentInstance
        fields = '__all__'


class EnvironmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EMR
        fields = '__all__'
