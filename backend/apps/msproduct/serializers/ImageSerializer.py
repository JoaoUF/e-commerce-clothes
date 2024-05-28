from msproduct.models import Image
from rest_framework import serializers

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        field = ['id', 'title', 'description', 'slug', 'upload']