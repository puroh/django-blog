from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from djangoblog.mixins import MixinComunFields


STATUS = (
    (0, "Draft"),
    (1, "Publish"),
)


class Post(MixinComunFields):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    # categories = models.ManyToManyField(Category)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
