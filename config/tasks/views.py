from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
        due_date = request.POST.get('due_date')

        Task.objects.create(
            title=title,
            user=request.user,
            due_date=due_date if due_date else None
        )
        return redirect('tasks_home')

    return render(request, 'tasks/add_task.html')

#update task
@login_required
def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('tasks_home')

#delete 
@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('tasks_home')