from rest_framework.serializers import ModelSerializer

from mushtra.models import Task, Result


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'title', 'description', 'active', 'user', 'schedule',
            'created_at'
        )


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = (
            'task', 'description', 'state', 'created_at'
        )
