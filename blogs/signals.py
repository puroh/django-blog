import uuid
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from blogs.models import Post


@receiver(pre_save, sender=Post)
def set_slug(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Post.objects.filter(slug=slug).exists():
            slug = slugify("{}-{}".format(instance.title, str(uuid.uuid4)[:8]))
    else:
        slug = instance.slug
    instance.slug = slug
