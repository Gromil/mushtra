from django.contrib.auth.models import User
from django.db import models

from .entity import Entity


class Profile(Entity):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
