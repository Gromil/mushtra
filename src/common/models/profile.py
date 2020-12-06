from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .entity import Entity


class Profile(Entity):
    user = models.OneToOneField(
        to=User, verbose_name=_('user'), help_text=_('user'),
        on_delete=models.CASCADE, related_name='profile',
    )
    age = models.IntegerField(default=30)
    name = models.CharField(default='', max_length=255)
    nick = models.CharField(default='', max_length=255)

    class Meta:
        db_table = 'common.profiles'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
