from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from webapp.models import Task, STATUS
from django.http import HttpResponseRedirect


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
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        new_task = Task.objects.create(title=title,  status=status, deadline=deadline)
        # return render(request, 'task_view.html', {'tasks': new_task})
        return HttpResponseRedirect(f'/task/{new_task.pk}')