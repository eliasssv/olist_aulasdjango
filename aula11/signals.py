from django.db.models.signals import pre_save
from .models import Carro
from slugify import slugify
from django.dispatch import receiver

@receiver(pre_save, sender=Carro)
def make_slugify(sender, instance, **kwargs):
    instance.slug = slugify(f"{instance.marca} {instance.modelo}")
