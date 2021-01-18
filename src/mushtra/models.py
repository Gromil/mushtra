from django.contrib.auth.models import User
from django.db import models

from common.models.entity import Entity


class Task(Entity):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title


class Schedule(models.Model):
    DAY_CHOICES = (
        ('mon', 'Понедельник'),
        ('tue', 'Вторник'),
        ('wed', 'Среда'),
        ('thu', 'Четверг'),
        ('fri', 'Пятница'),
        ('sat', 'Суббота'),
        ('sun', 'Воскресенье'),
    )

    day = models.CharField('День недели', max_length=3, choices=DAY_CHOICES)
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.task.title} - {self.day}'
