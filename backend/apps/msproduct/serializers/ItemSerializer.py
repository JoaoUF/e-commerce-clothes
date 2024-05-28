from msproduct.models import Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        field = ['id', 'quantity', 'total', 'bill', 'product']