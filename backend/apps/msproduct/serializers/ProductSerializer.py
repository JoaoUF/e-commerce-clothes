from msproduct.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['id', 'title', 'description', 'slug', 'price']