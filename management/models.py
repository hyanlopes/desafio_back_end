import uuid

from django.db import models


class Management(models.Model):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    type = models.CharField(max_length=22)
    date = models.CharField(max_length=10)
    value = models.IntegerField()
    cpf = models.IntegerField()
    card = models.CharField(max_length=20)
    hour = models.CharField(max_length=8)
    store_property = models.CharField(max_length=30)
    store_name = models.CharField(max_length=30)
    store_id = models.ForeignKey(
        "store.Store", on_delete=models.CASCADE, related_name="Management"
    )


# Create your models here.
