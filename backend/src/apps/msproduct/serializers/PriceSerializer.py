from msproduct.models import Price
from rest_framework import serializers


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["id", "color", "size", "product", "originalPrice", "discountPrice"]


class PriceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["id", "color", "size", "product", "originalPrice", "discountPrice"]
        depth = 1
