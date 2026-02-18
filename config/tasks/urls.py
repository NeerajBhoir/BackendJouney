from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks_home, name='tasks_home'),
    path('add/', views.add_task, name='add_task'),
]
