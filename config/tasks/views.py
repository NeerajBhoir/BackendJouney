from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required


# show tasks
@login_required
def tasks_home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# create task
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            completed=False
        )
        return redirect('tasks_home')

    return render(request, 'tasks/add_task.html')