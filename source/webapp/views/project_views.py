from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from django.urls import reverse
from webapp.forms import ProjectForm
from webapp.models import Project, Task


class TaskProjectCreateView(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.task.pk})

    def form_valid(self, form):
        task = get_object_or_404(Task, pk=self.kwargs.get('pk'))
        form.instance.task = task
        return super().form_valid(form)
