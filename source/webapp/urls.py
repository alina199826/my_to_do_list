from webapp.views import IndexViews, ProjectView, ProjectDeleteView,  TaskUpdateView, IndexViewsProject, TaskCreateView, TaskView, MyRedirectView, ProjectUpdateView,  TaskDeleteView, TaskProjectCreateView

from django.urls import path
from django.views.generic import RedirectView

app_name = 'webapp'



urlpatterns = [
    path('', RedirectView.as_view(pattern_name='webapp:index_project')),
    path('task/', IndexViews.as_view(), name='webapp:index'),
    path('project/', IndexViewsProject.as_view(), name='webapp:index_project'),
    path('task/<int:pk>/', TaskView.as_view(), name='webapp:view'),
    path('project/<int:pk>/', ProjectView.as_view(), name='webapp:project_view'),
    path('task/project/add', TaskProjectCreateView.as_view(), name='webapp:project_add'),
    path('task/add/', TaskCreateView.as_view(), name='webapp:create'),
    path('task/<int:pk>/update/', TaskUpdateView.as_view(), name='webapp:update'),
    path('project/<int:pk>/update/', ProjectUpdateView.as_view(), name='webapp:project_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='webapp:delete'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='webapp:project_delete'),

]