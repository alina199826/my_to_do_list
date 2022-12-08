
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import RedirectView, FormView, ListView, DetailView, CreateView



class IndexViews(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ('-created_at',)
    paginate_by = 5
    search_form_class = SimpleSearchForm
    search_fields = ['summary__icontains', 'description__icontains']



    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class TaskView(DetailView):
    template_name = 'task_view.html'
    model = Task



class MyRedirectView(RedirectView):
    url = 'https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/RedirectView/'


class TaskCreateView(CreateView):
    template_name = "create.html"
    model = Task

    form_class = TaskForm



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


