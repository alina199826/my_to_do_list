from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS
from webapp.forms import TaskForm


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
        form = TaskForm()
        return render(request, "create.html", {'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                deadline=form.cleaned_data['deadline'],
                status=form.cleaned_data['status']
            )
            return redirect('view', pk=new_task.pk)
        else:
            return render(request, "create.html", {'form': form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'deadline': task.deadline,
            'status': task.status,
        })
        return render(request, 'task_update.html', {'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.deadline = form.cleaned_data.get('deadline')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.save()
            return redirect('view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'form': form})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')
