from msproduct.models import Size
from msproduct.serializers import SizeSerializer
from rest_framework import generics

class SizeList(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class SizeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer