from msproduct.models import Color
from rest_framework import serializers

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        field = ['id', 'name']
