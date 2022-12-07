
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils.http import urlencode
from webapp.models import Task
from webapp.forms import TaskForm, SimpleSearchForm, TaskDeleteForm
from django.views.generic import RedirectView, DeleteView, ListView, DetailView, CreateView, UpdateView


class IndexViews(ListView):
    template_name = 'index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ('-created_at',)
    paginate_by = 10

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



class TaskUpdateView(UpdateView):
    template_name = "task_update.html"
    form_class = TaskForm
    model = Task
    context_object_name = 'task'


class TaskDeleteView(DeleteView):
    template_name = 'task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('index')
    form_class = TaskDeleteForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


