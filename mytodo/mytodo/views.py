from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem
from django.db import connection

def index(request):
    if request.method == 'POST':
        task_text = request.POST.get('task_text')
        if task_text:
            new_task = TodoItem(title=task_text)
            new_task.save()
            return redirect('index')
    else:
        tasks = TodoItem.objects.all()
        return render(request, 'index.html', {'tasks': tasks})

def delete_task(request, task_id):
    task = get_object_or_404(TodoItem, pk=task_id)
    if request.method == 'POST':
        task.delete()
    return redirect('index')

def check_task(request, task_id):
    task = get_object_or_404(TodoItem, pk=task_id)
    if request.method == 'POST':
        task.completed = not task.completed
        task.save()
    return redirect('index')
