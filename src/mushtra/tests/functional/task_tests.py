from django.test import Client
from requests import Response

from mushtra.models import Task


def test_tasks_get(db, authorized_client: Client, task: Task) -> None:
    response: Response = authorized_client.get(path='/api/tasks/')
    assert response.status_code == 200
    # TODO: freeze time and check for response


def test_tasks_create(db, authorized_client: Client) -> None:
    response: Response = authorized_client.post(
        path='/api/tasks/', data={
            'title': 'reading', 'description': '10 minute',
        }
    )
    assert response.status_code == 201
    assert Task.objects.count() == 1
    assert str(Task.objects.last()) == 'reading'
