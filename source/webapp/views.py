from django.shortcuts import render, redirect, get_object_or_404
from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic import View, TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context



class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context

# def create_task(request):
#     if request.method == "GET":
#         form = TaskForm()
#         return render(request, "create.html", {'form': form})
#     elif request.method == "POST":
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             new_task = Task.objects.create(
#                 summary=form.cleaned_data['summary'],
#                 description=form.cleaned_data['description'],
#                 type=form.cleaned_data['type'],
#                 status=form.cleaned_data['status'],
#
#             )
#             return redirect('view', pk=new_task.pk)
#         else:
#             return render(request, "create.html", {'form': form})

class CreateTask(TemplateView):
    template_name = 'create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['form'] = TaskForm
        return context


    def post(self, request, *args, **kwargs):
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = Task.objects.create(**form.cleaned_data)
            return redirect('view', pk=task.pk)
        else:
            context = self.get_context_data(**kwargs)
            context['form'] = form
            return self.render_to_response(context)


# def task_update(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == 'GET':
#         form = TaskForm(initial={
#             'summary': task.summary,
#             'description': task.description,
#             'type': task.type,
#             'status': task.status,
#             'created_at': task.created_at,
#             'updated_at': task.updated_at
#         })
#         return render(request, 'task_update.html', {'form': form})
#     elif request.method == "POST":
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.summary = form.cleaned_data.get('summary')
#             task.type = form.cleaned_data.get('type')
#             task.description = form.cleaned_data.get('description')
#             task.status = form.cleaned_data.get('status')
#             task.created_at = form.cleaned_data.get('created_at')
#             task.updated_at = form.cleaned_data.get('updated_at')
#             task.save()
#             return redirect('view', pk=task.pk)
#         else:
#             return render(request, 'task_update.html', {'form': form})

class TaskUpdate(View):

    def get (self, request, *args,**kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(initial={
            'summary': task.summary,
            'description': task.description,
            'status': task.status,
            'type': task.type
        })
        return render(request, 'task_update.html', {'form': form, 'task': task})

    def post(self, request, *args,**kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.summary = form.cleaned_data['summary']
            task.description = form.cleaned_data['description']
            task.status = form.cleaned_data['status']
            task.type = form.cleaned_data['type']
            task.save()
            return redirect('view', pk=task.pk)
        else:
            render(request, 'task_update.html', {'form': form, 'task': task})


# def task_delete(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == "GET":
#         return render(request, 'task_delete.html', {'task': task})
#     elif request.method == "POST":
#         task.delete()
#         return redirect('index')


class TaskDelete(View):
    def get(self, request, *args,**kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return  render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args,**kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')
