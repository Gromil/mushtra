from django.contrib.auth.models import User
from django.db import models

from common.models.entity import Entity


class Task(Entity):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    schedule = models.JSONField(default={})

    def __str__(self):
        return self.title


class Result(Entity):
    DONE = 'done'
    SKIPPED = 'skipped'
    FAILED = 'failed'
    INACTIVE = 'inactive'

    STATES = (
        (DONE, 'done'),
        (SKIPPED, 'skipped'),
        (FAILED, 'failed'),
        (INACTIVE, 'inactive')
    )

    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=255, default='')
    state = models.CharField(choices=STATES, max_length=125)
