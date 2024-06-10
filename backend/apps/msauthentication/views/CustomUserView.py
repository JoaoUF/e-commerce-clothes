from django.conf import settings
import jwt
from msauthentication.serializers import RegisterSerializer, ChangePasswordSerializer, LogInSerializer, VerifyEmailSerializer
from msauthentication.models import CustomUser
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.views import TokenObtainPairView


class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LogoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)

class VerifyEmailView(APIView):
    serializer_class = VerifyEmailSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        token = request.GET.get('access')
        print('TOKEN', type(token))
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            customUser = CustomUser.objects.get(id=payload['user_id'])
            if not customUser.is_verified:
                customUser.is_verified = True
                customUser.save()
                return Response({'email': 'Successfully activated.'},status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Already active'}, status=status.HTTP_406_NOT_ACCEPTABLE)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Token expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            print('ERROR', identifier)
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
