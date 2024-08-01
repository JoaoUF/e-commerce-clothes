from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_framework.permissions import AllowAny
from django.conf import settings


class GoogleLogin(SocialLoginView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
    callback_url = settings.CALL_BACK_URL
    client_class = OAuth2Client


class GoogleLoginVersionTwo(SocialLoginView):
    permission_classes = (AllowAny,)
    authentication_classes = []
    adapter_class = GoogleOAuth2Adapter
