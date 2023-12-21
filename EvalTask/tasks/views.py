from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from .tasks import print_task_name

class CreateTaskView(generics.CreateAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        task = serializer.save(user=self.request.user)
        
        # Trigger the Celery task with the task name
        print_task_name.apply_async(args=[task.task_name], eta=task.created_at)

class ListTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

