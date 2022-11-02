from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ShippingClaim, ClaimDoc
from .utils import create_doc


@receiver(post_save, sender=ShippingClaim)
def create_claim_doc(sender, instance, created, **kwargs):
    if created:
        create_doc(object=ClaimDoc, instance=instance)