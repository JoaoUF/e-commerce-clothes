from rest_framework import serializers
from msauthentication.models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from msemailmodule.utils.Email import select_subject

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(queryset=CustomUser.objects.all())] # type: ignore
    )
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'password2')

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    'error': 'Password field did not match'
                }
            )
        return attrs
    
    def create(self, validated_data):
        customUser = CustomUser.objects.create_user( # type: ignore
            email = validated_data['email'],
            password = validated_data['password']
        )
        select_subject(
            option=1,
            email=validated_data["email"],
            custom_user=customUser
        )
        return customUser