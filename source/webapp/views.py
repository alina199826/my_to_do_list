from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic import View
from django.views.generic import TemplateView, RedirectView, FormView
from webapp.base_views import FormView as CustomFormView


# class IndexView(TemplateView):
#     template_name = 'index.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['tasks'] = Task.objects.all()
#         return context
#
#     def post(self, request, *args, **kwargs):
#         for task_pk in request.POST.getlist('tasks'):
#             Task.objects.get(pk=task_pk).delete()
#         context = self.get_context_data(**kwargs)
#         return self.render_to_response(context)
#
#
#
#
# class TaskView(TemplateView):
#     template_name = 'task_view.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
#
#         return context
#
#
#
#
# class CreateTask(TemplateView):
#     template_name = 'create.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['form'] = TaskForm
#         return context
#
#
#     def post(self, request, *args, **kwargs):
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             type = form.cleaned_data.pop('type')
#             task = Task.objects.create(**form.cleaned_data)
#             task.type.set(type)
#             return redirect('view', pk=task.pk)
#         else:
#             context = self.get_context_data(**kwargs)
#             context['form'] = form
#             return self.render_to_response(context)
#
#
#
# class TaskUpdate(View):
#
#     def get (self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs['pk'])
#         form = TaskForm(initial={
#             'summary': task.summary,
#             'description': task.description,
#             'status': task.status,
#             'type': task.type.all(),
#         })
#         return render(request, 'task_update.html', {'form': form, 'task': task})
#
#     def post(self, request, *args, **kwargs):
#         task = get_object_or_404(Task, pk=kwargs['pk'])
#         form = TaskForm(data=request.POST)
#         if form.is_valid():
#             task.summary = form.cleaned_data['summary']
#             task.description = form.cleaned_data['description']
#             task.status = form.cleaned_data['status']
#             task.save()
#             task.type.set(form.cleaned_data['type'])
#             return redirect('view', pk=task.pk)
#         else:
#             render(request, 'task_update.html', {'form': form, 'task': task})


class IndexViews(View):
    def get(self, request, *args, **kwargs):
        tasks = Task.objects.order_by('-created_at')
        context = {
            'tasks': tasks
        }
        return render(request, "index.html", context)

    def post(self, request, *args, **kwargs):
        for task_pk in request.POST.getlist('tasks'):
            Task.objects.get(pk=task_pk).delete()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        kwargs['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return super().get_context_data(**kwargs)


class MyRedirectView(RedirectView):
    url = 'https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/RedirectView/'


class TaskCreateView(CustomFormView):
    template_name = "create.html"
    form_class = TaskForm

    def get_redirect_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)


class TaskUpdateView(FormView):
    template_name = "task_update.html"
    form_class = TaskForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.task.pk})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', {'task': task})
    elif request.method == "POST":
        task.delete()
        return redirect('index')


