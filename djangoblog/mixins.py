from django.db import models
from uuid import uuid4


class MixinComunFields(models.Model):
    id = models.UUIDField(max_length=255, default=uuid4, primary_key=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
