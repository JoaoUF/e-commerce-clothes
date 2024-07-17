from msproduct.models import Price
from msproduct.serializers import PriceSerializer, PriceDetailSerializer
from rest_framework import generics


class PriceList(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    search_fields = ["product"]


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetailList(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceDetailSerializer
    search_fields = ["product"]
