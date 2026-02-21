from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required


# SHOW TASKS (only logged in user's tasks)
@login_required
def tasks_home(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


# CREATE TASK
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')

        Task.objects.create(
            title=title,
            description=description,
            user=request.user,
            due_date=due_date if due_date else None
        )
        return redirect('tasks_home')

    return render(request, 'tasks/add_task.html')


# EDIT TASK (SECURE)
@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.due_date = request.POST.get('due_date')
        task.save()
        return redirect('tasks_home')

    return render(request, 'tasks/edit_task.html', {'task': task})


# TOGGLE COMPLETE
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks_home')


# DELETE TASK (SECURE + CONFIRMATION)
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('tasks_home')

    return render(request, 'tasks/delete_task.html', {'task': task})