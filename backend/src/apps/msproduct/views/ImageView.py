from msproduct.models import Image, Product
from msproduct.serializers import ImageSerializer, ImageDetailSerializer
from rest_framework import generics


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class ImageProductListDetail(generics.ListAPIView):
    serializer_class = ImageDetailSerializer

    def get_object(self):
        list_detail = []
        for i in Product.objects.all():
            list_detail.append(Image.objects.filter(id=i.id).first())
        return list_detail
