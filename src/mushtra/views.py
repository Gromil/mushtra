from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from mushtra.models import Task, Result
from mushtra.serializers import TaskSerializer, ResultSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    permission_classes = (IsAuthenticated,)
