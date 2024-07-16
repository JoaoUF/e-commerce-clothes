from msauthentication.models import CustomUser
from msproduct.models import Bill
from django.dispatch import receiver
from allauth.account.signals import email_confirmed


@receiver(email_confirmed)
def assign_bill_after_user_creation(request, email_address, **kwargs):
    print("PRIMER SIGNAL")
    current_user = CustomUser.objects.get(email=email_address)
    new_bill = Bill(user=current_user)
    new_bill.save()
