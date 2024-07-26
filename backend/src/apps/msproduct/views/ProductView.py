from msproduct.models import Product, Price, Image
from msproduct.serializers import (
    ProductSerializer,
    PriceDetailSerializer,
    ImageSerializer,
)
from rest_framework import generics
from rest_framework import filters
from rest_framework.views import APIView, Response
from rest_framework.permissions import AllowAny


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.active()  # type: ignore
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.active()  # type: ignore
    serializer_class = ProductSerializer


class SingleProductDetail(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = []

    def get(self, request):
        queryset_price = Price.objects.filter(product=request.GET.get("product"))
        queryset_image = Image.objects.filter(product=request.GET.get("product"))  # type: ignore
        data = [
            {
                "prices": [
                    {**PriceDetailSerializer(price).data} for price in queryset_price  # type: ignore
                ],
                "images": [{**ImageSerializer(image).data} for image in queryset_image],  # type: ignore
            }
        ]
        return Response(data)
