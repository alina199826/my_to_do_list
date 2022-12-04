from django.db import models
from django.urls import reverse





class Status(models.Model):
    title = models.CharField(max_length=20, verbose_name='Статус')
    def __str__(self):
        return f'{self.pk}. {self.title}'


class Type(models.Model):
    title = models.CharField(max_length=20, verbose_name='Тип')
    def __str__(self):
        return f'{self.pk}. {self.title}'

class Task(models.Model):
    summary = models.CharField(max_length=500, null=False, blank=False, verbose_name="summary")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="description")
    status = models.ForeignKey('webapp.Status', related_name='status',  on_delete=models.PROTECT)
    type = models.ManyToManyField('webapp.Type', related_name='type',)


    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.pk})



    def __str__(self):
        return f'{self.pk}. {self.summary}'



class Project(models.Model):
    title = models.CharField(max_length=500, verbose_name="title")
    content = models.TextField(max_length=2000, verbose_name="content")
    date_start = models.DateField(verbose_name='the date of the beginning')
    date_end = models.DateField(null=True, blank=True, verbose_name='expiration date')
    project = models.ForeignKey('webapp.Project', on_delete=models.CASCADE, related_name='project_task',
                                verbose_name="project")