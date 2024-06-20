from rest_framework import serializers
from msauthentication.models import CustomUser
from django.contrib.auth.password_validation import validate_password

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only = True,
        required = True,
        validators = [validate_password]
    )
    password2 = serializers.CharField(
        write_only = True,
        required = True,
    )
    old_password = serializers.CharField(
        write_only = True,
        required = True,
    )

    class Meta:
        model = CustomUser
        fields = ('password', 'password2', 'old_password')

    def validate(self,attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    'error': 'Password field did not match'
                }
            )
        return attrs

    def validate_old_password(self, value):
        customUser = self.context['request'].customUser

        if not customUser.check_password(value):
            raise serializers.ValidationError(
                {
                    "old_password": "Old password is not correct"
                }
            )
        return value

    def update(self, instance, validated_data):
        customUser = self.context['request'].customUser

        if customUser.pk != instance.pk:
            raise serializers.ValidationError(
                {
                    'error': 'You do not have permission for this user'
                }
            )

        instance.set_password(validated_data['password'])
        instance.save()

        return instance
