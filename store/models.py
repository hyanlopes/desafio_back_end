import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Store(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)


# Create your models here.
