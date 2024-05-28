from msproduct.models import Size
from rest_framework import serializers

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        field = ['id', 'name']