from django.shortcuts import render
from .models import Task

def tasks_home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})
