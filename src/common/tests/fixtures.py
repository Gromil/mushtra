from django.contrib.auth.models import User
from django.test import Client
from pytest import fixture
from rest_framework.authtoken.models import Token


@fixture
def user():
    return User.objects.create(username='lol', password='pass')


@fixture
def authorized_client(client: Client, user: User):
    token = Token.objects.get_or_create(user=user)[0].key
    client.defaults['HTTP_AUTHORIZATION'] = f'Token {token}'
    return client
