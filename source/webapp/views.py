from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from webapp.models import Task, STATUS


def index_views(request):
    if request.method == 'POST':
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
    tasks = Task.objects.all()
    return render(request, "index.html", {'tasks' : tasks})


# def article_view(request):
#     article_id = request.GET.get('id')
#     article = Article.objects.get(pk=article_id)
#     context = {'article': article}
#     return render(request, 'article_view.html', context)


# def article_create_view(request):
#     if request.method == "GET":
#         return render(request, "create.html", {'statuses': STATUS})
#     elif request.method == "POST":
#         title = request.POST.get('title')
#         status = request.POST.get('status')
#         deadline = request.POST.get('deadline')
#         new_task = Article.objects.create(title=title,  status=status, deadline=deadline)
#         return render(request, 'task_view.html', {'tasks' : tasks})
#


def create_task(request):
    if request.method == "GET":
        return render(request, "create.html", {'statuses': STATUS})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        new_task = Task.objects.create(title=title,  status=status, deadline=deadline)
        return render(request, 'task_view.html', {'tasks': new_task})
