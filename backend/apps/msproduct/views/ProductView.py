from msproduct.models import Product
from msproduct.serializers import ProductSerializer
from rest_framework import generics
from rest_framework import filters

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.activate() # type: ignore
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.activate() # type: ignore
    serializer_class = ProductSerializer