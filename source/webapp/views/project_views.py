from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Q
from django.utils.http import urlencode
from django.shortcuts import reverse
from webapp.models import Project
from django.urls import reverse_lazy
from webapp.forms import SimpleSearchForm, ProjectForm, ProjectDeleteForm
from django.views.generic import RedirectView, DeleteView, ListView, DetailView, CreateView, UpdateView



class TaskProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm


    def form_valid(self, form):
        users = User.objects.filter()
        form.instance.users = self.request.user
        return super().form_valid(form)


    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class IndexViewsProject(ListView):
    template_name = 'project/project_list.html'
    context_object_name = 'projects'
    model = Project
    ordering = ('-date_start',)
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



class ProjectUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = "project/project_update.html"
    form_class = ProjectForm
    model = Project
    context_object_name = 'project'
    permission_required = 'webapp.change_project'

    def has_permission(self):
        return super().has_permission() or self.get_object().users == self.request.user


class ProjectDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = Project
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:index_project')
    form_class = ProjectDeleteForm
    permission_required = 'webapp.delete_project'

    def has_permission(self):
        return super().has_permission() or self.get_object().users == self.request.user

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(instance=self.object, data=request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


