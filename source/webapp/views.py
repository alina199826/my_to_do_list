from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task, STATUS


def index_views(request):
    if request.method == 'POST':
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
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