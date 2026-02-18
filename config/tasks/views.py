from django.shortcuts import render, redirect
from .models import Task

# list all tasks
def tasks_home(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# create a new task
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            title=title,
            description=description,
            completed=False
        )
        return redirect('tasks_home')

    return render(request, 'tasks/add_task.html')
