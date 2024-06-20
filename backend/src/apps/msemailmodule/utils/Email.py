from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from msemailmodule.tasks.SendMail import send_email

def select_subject(option: int,email: str, custom_user) -> None:
    match option:
        case 1:
            token = RefreshToken.for_user(custom_user).access_token # type: ignore
            absurl = f'{settings.HOST_URL_SITE}/verify-email?token={token}'
            html = f'Hello {custom_user.email}! \n Use link below to verify email {absurl}'

            subject = "Verify email"
        case 2:
            # correo de cambio de contraseña
            pass
        case 3:
            # correo de verificacion de recibo de compra
            pass
    send_email.delay(email, html, subject)
