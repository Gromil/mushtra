from django.contrib.auth.models import User
from django.test import Client
from requests import Response

from common.models import Profile


def test_profile_create(db, client: Client) -> None:
    response: Response = client.post(
        path='/api/profiles/', data={'username': 'lol', 'password': 'pass'}
    )
    assert response.status_code == 201

    assert Profile.objects.count() == 1
    assert str(Profile.objects.last()) == 'lol'


def test_profile_exists(db, client: Client, user: User) -> None:
    response: Response = client.post(
        path='/api/profiles/', data={'username': 'lol', 'password': 'pass'}
    )
    assert response.status_code == 400
    assert response.json() == ['username already exists']
