from __future__ import absolute_import, unicode_literals
from celery import shared_task
from allauth.account.utils import setup_user_email


@shared_task()
def send_mail(request, user, user_list) -> None:
    setup_user_email(request, user, user_list)
