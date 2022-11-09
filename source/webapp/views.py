from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS


def index_views(request):
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks': tasks})


def task_view(request, pk):
    # task_id = kwargs.get('id')
    task = Task.objects.get(pk=pk)
    context = {'task': task}
    return render(request, 'task_view.html', context)

def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS})
    elif request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        new_task = Task.objects.create(title=title, description=description,  status=status, deadline=deadline)
        return redirect('view', pk=new_task.pk)

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_update.html', {'task': task})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.save()
        return redirect('view', pk=task.pk)

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')
