from msproduct.models import Price
from msproduct.serializers import PriceSerializer
from rest_framework import generics

class PriceList(generics.ListCreateAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class PriceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer