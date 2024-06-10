from rest_framework import serializers
from msauthentication.models import CustomUser

class VerifyEmailSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=555)