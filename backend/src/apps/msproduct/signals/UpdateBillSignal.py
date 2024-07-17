from msproduct.models import Bill
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Bill)
def create_new_bill_after_checkout(sender, instance, created, weak=False, **kwargs):
    if not created:
        new_bill = Bill(user=instance.user)
        new_bill.save()
