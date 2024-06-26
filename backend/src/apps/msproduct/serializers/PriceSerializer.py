from msproduct.models import Price
from rest_framework import serializers

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['id', 'color', 'size', 'originalPrice', 'discountPrice']