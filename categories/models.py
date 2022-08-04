from django.db import models

from djangoblog.mixins import MixinComunFields


class Category(MixinComunFields):
    title = models.CharField(max_length=20)
    subtitle = models.CharField(max_length=20)
    slug = models.SlugField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
