from msproduct.models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "quantity", "bill", "price"]


class ItemDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "quantity", "price"]
        depth = 2
