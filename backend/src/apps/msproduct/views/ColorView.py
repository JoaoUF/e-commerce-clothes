from msproduct.models import Color
from msproduct.serializers import ColorSerializer
from rest_framework import generics

class ColorList(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

class ColorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer