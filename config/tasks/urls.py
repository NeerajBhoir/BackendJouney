from django.urls import path
from . import views
from .views import TaskListCreateAPI, TaskDetailAPI

urlpatterns = [
    path('', views.tasks_home, name='tasks_home'),
    path('add/', views.add_task, name='add_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    path('api/tasks/', TaskListCreateAPI.as_view(), name='api_tasks'),
    path('api/tasks/<int:pk>/', TaskDetailAPI.as_view(), name='api_task_detail'),
]
