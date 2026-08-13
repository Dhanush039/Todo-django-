from django.shortcuts import render, redirect, get_object_or_404
from .models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False)
    completed_tasks = Task.objects.filter(is_completed=True)

    context = {
        'tasks': tasks,
        'completed_tasks': completed_tasks,
    }

    return render(request, 'home.html', context)


def addTask(request):
    if request.method == 'POST':
        task = request.POST.get('task')

        if task:
            Task.objects.create(task=task)

    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.is_completed = True
    task.save()

    return redirect('home')


def mark_as_undone(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.is_completed = False
    task.save()

    return redirect('home')


def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    task.delete()

    return redirect('home')


def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        new_task = request.POST.get('task')

        if new_task:
            task.task = new_task
            task.save()

        return redirect('home')

    return render(request, 'edit.html', {'task': task})