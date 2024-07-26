from msproduct.models import Price
from rest_framework import serializers
from .ImageSerializer import ImageSerializer
from msproduct.models import Image


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ["id", "color", "size", "product", "originalPrice", "discountPrice"]


class PriceDetailSerializer(serializers.ModelSerializer):
    # images = serializers.SerializerMethodField()

    class Meta:
        model = Price
        fields = [
            "id",
            "color",
            "size",
            "originalPrice",
            "discountPrice",
        ]
        depth = 1

    # def get_images(self, prices):
    #     return [
    #         {**ImageSerializer(item).data}  # type: ignore
    #         for item in Image.objects.filter(product=prices.product.id)
    #     ]
