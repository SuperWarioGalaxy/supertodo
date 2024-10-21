from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.text import slugify

from .forms import AddTaskForm, EditTaskForm
from .models import Task


# Create your views here.
def task_list(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    num_d = tasks.filter(done=True).count()
    num_f = tasks.filter(done=False).count()
    return render(
        request,
        'tasks/list.html',
        {'num_tasks': num_tasks, 'tasks': tasks, 'num_d': num_d, 'num_f': num_f},
    )


def task_detail(request: HttpRequest, slug: str) -> HttpResponse:
    task = Task.objects.get(slug=slug)
    return render(request, 'tasks/detail.html', dict(task=task))


def add_task(request):
    if request.method == 'POST':
        if (form := AddTaskForm(request.POST)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:add-task')
    else:
        form = AddTaskForm()
    return render(request, 'tasks/add_task.html', dict(form=form))


def task_toggle(request, slug: str):
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()

    task = Task.objects.get(slug=slug)
    if task.done:
        task.done = False
        task.save()
    else:
        task.done = True
        task.save()
    num_d = tasks.filter(done=True).count()
    num_f = tasks.filter(done=False).count()
    return render(
        request,
        'tasks/list.html',
        {'num_tasks': num_tasks, 'tasks': tasks, 'num_d': num_d, 'num_f': num_f},
    )


def task_edit(request, slug: str):
    task = Task.objects.get(slug=slug)
    if request.method == 'POST':
        if (form := EditTaskForm(request.POST, instance=task)).is_valid():
            task = form.save(commit=False)
            task.slug = slugify(task.name)
            task.save()
            return redirect('tasks:task-list')
    else:
        form = EditTaskForm(instance=task)
    return render(request, 'tasks/edit.html', dict(task=task, form=form))


def task_delete(request, slug: str):
    Task.objects.filter(slug=slug).delete()
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    num_d = tasks.filter(done=True).count()
    num_f = tasks.filter(done=False).count()
    return render(
        request,
        'tasks/list.html',
        {'num_tasks': num_tasks, 'tasks': tasks, 'num_d': num_d, 'num_f': num_f},
    )


def show_done(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    tasks_d = tasks.filter(done=True)
    num_d = tasks.filter(done=True).count()
    num_f = tasks.filter(done=False).count()
    return render(
        request,
        'tasks/list.html',
        {'num_tasks': num_tasks, 'tasks': tasks_d, 'num_d': num_d, 'num_f': num_f},
    )


def show_pending(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()
    tasks = Task.objects.all()
    tasks_f = tasks.filter(done=False)
    num_d = tasks.filter(done=True).count()
    num_f = tasks.filter(done=False).count()
    return render(
        request,
        'tasks/list.html',
        {'num_tasks': num_tasks, 'tasks': tasks_f, 'num_d': num_d, 'num_f': num_f},
    )
