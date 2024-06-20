from msproduct.models import ProductImage
from msproduct.serializers import ProductImageSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class ProductImageList(generics.ListCreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['product']

class ProductImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
