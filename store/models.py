import uuid

from django.db import models


class Store(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=30)


# Create your models here.
