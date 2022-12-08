
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import  Project
from webapp.forms import SimpleSearchForm, ProjectForm
from django.views.generic import RedirectView, FormView, ListView, DetailView, CreateView


class TaskProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.object.pk})


class IndexViewsProject(ListView):
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('title',)
    paginate_by = 5
    search_form_class = SimpleSearchForm
    search_fields = ['title__icontains', 'content__icontains']

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
            queryset = queryset.filter(Q(title__icontains=self.search_value) | Q(content__icontains=self.search_value))
        return queryset


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = Project



class MyRedirectView(RedirectView):
    url = 'https://ccbv.co.uk/projects/Django/4.1/django.views.generic.base/RedirectView/'



class ProjectUpdateView(FormView):
    template_name = "project/project_update.html"
    form_class = ProjectForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Project, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.project = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['project'] = self.project
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.project
        return kwargs

    def form_valid(self, form):
        self.project = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.project.pk})


def project_delete_view(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == "GET":
        return render(request, 'project/project_delete.html', {'project': project})
    elif request.method == "POST":
        project.delete()
        return redirect('index_project')



