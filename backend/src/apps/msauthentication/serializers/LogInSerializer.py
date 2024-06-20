from rest_framework import exceptions
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from msauthentication.models import CustomUser


class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            customUser = CustomUser.objects.get(email=attrs.get('email'))
            if customUser.check_password(attrs.get('password')): # type: ignore
                if not customUser.is_verified: # type: ignore
                    raise exceptions.AuthenticationFailed('User is deactivated')

                data = {}
                refresh = self.get_token(customUser)

                data['refresh'] = str(refresh)
                data['access'] = str(refresh.access_token) # type: ignore

                return data
            else:
                return 'Incorrect password'
        except CustomUser.DoesNotExist:
            return ('This email was not found on the database.')