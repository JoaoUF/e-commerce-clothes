from msproduct.models import Price
from msproduct.serializers import PriceSerializer, PriceDetailSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class PriceList(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class PriceDetailList(generics.ListAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceDetailSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["product"]
