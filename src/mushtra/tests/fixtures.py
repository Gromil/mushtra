from django.contrib.auth.models import User
from pytest import fixture

from mushtra.models import Task


@fixture
def task(user: User):
    return Task.objects.create(
        title='laundry', description='do laundry please', user=user
    )
