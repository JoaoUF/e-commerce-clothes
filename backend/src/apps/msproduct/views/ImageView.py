from msproduct.models import Image, Product
from msproduct.serializers import ImageSerializer, ImageDetailSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageProductListDetail(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ImageDetailSerializer

    def get_queryset(self):
        queryset = Image.objects.none()
        product_uuid_list = Product.objects.values("id")
        for i in product_uuid_list:
            instance = Image.objects.filter(product=i["id"]).first()
            queryset |= Image.objects.filter(id=instance.id)  # type: ignore
        return queryset
