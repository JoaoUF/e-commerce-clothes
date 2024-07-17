from msproduct.models import Item
from msproduct.serializers import ItemSerializer, ItemDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetailList(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["bill"]
