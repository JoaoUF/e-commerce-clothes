from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


class CustomAccountAdapter(DefaultAccountAdapter):

    def get_email_confirmation_url(self, request, emailconfirmation):
        url = f"{settings.EMAIL_CONFIRM_REDIRECT_BASE_URL}{emailconfirmation}"
        return url
