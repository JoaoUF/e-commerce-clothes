from __future__ import absolute_import, unicode_literals

from django.core.mail import EmailMessage
from celery import shared_task

@shared_task
def send_email(email: str, html: str, subject: str) -> None:
    print('ENVIANDO EMAIL')
    sender = EmailMessage(
        subject= subject,
        body= html,
        to = [email]
    )
    sender.send()