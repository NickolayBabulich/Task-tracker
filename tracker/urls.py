from django.urls import path
from tracker.views import (TaskCreateAPIView,
                           TaskUpdateAPIView,
                           TaskDestroyAPIView,
                           TaskListAPIView,
                           PerformerViewSet,
                           ProjectViewSet)
from tracker.apps import TrackerConfig
from rest_framework.routers import DefaultRouter

app_name = TrackerConfig.name

router = DefaultRouter()
router.register(r'performer', PerformerViewSet, basename='performer')
router.register(r'project', ProjectViewSet, basename='project')

urlpatterns = [
    path('task/create/', TaskCreateAPIView.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskUpdateAPIView.as_view(), name='update_task'),
    path('task/destroy/<int:pk>/', TaskDestroyAPIView.as_view(), name='delete_task'),
    path('task/list/', TaskListAPIView.as_view(), name='tasks')
]

urlpatterns += router.urls
