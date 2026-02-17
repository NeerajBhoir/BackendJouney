from django.urls import path
from .views import tasks_home

urlpatterns = [
    path('', tasks_home),
]
