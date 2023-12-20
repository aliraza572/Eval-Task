from django.urls import path
from .views import CreateTaskView, ListTasksView

urlpatterns = [
    path('create-task/', CreateTaskView.as_view(), name='create-task'),
    path('list-tasks/', ListTasksView.as_view(), name='list-tasks'),
]