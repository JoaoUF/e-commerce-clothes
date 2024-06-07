from msemailmodule.models import Template
from msemailmodule.serializers import TemplateSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny

class TemplateList(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

class TemplateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (AllowAny,)