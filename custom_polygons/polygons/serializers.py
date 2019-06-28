from rest_framework import serializers
from .models import Polygon, Provider

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'

class PolygonSerializer(serializers.ModelSerializer):

    choices = ProviderSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Polygon
        fields = '__all__'


