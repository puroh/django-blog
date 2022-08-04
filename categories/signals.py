import uuid
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from categories.models import Category


@receiver(pre_save, sender=Category)
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Category.objects.filter(slug=slug).exists():
            slug = slugify("{}-{}".format(instance.title, str(uuid.uuid4)[:8]))
    instance.slug = slug
