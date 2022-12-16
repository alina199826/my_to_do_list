from webapp.views import IndexViews, ProjectView, ProjectDeleteView,  TaskUpdateView, IndexViewsProject, TaskCreateView, TaskView, MyRedirectView, ProjectUpdateView,  TaskDeleteView, TaskProjectCreateView

from django.urls import path
from django.views.generic import RedirectView

app_name = 'webapp'



urlpatterns = [
    path('', RedirectView.as_view(pattern_name='webapp:index_project')),
    path('task/', IndexViews.as_view(), name='index'),
    path('project/', IndexViewsProject.as_view(), name='index_project'),
    path('task/<int:pk>/', TaskView.as_view(), name='view'),
    path('project/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('task/project/add', TaskProjectCreateView.as_view(), name='project_add'),
    path('task/add/', TaskCreateView.as_view(), name='create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='project_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),

]