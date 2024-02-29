from rest_framework.generics import (CreateAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView,
                                     ListAPIView)
from rest_framework import viewsets
from tracker.models import (Task,
                            Performer,
                            Project)
from tracker.serializers import (TaskSerializer,
                                 PerformerSerializer,
                                 ProjectSerializer)


class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskCreateAPIView(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPIView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDestroyAPIView(DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class PerformerViewSet(viewsets.ModelViewSet):
    queryset = Performer.objects.all()
    serializer_class = PerformerSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
