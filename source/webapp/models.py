from django.db import models


# Create your models here.


class Status(models.Model):
    title = models.CharField(max_length=20, verbose_name='Статус')
    def __str__(self):
        return f'{self.pk}. {self.title}'


class Type(models.Model):
    title = models.CharField(max_length=20, verbose_name='Тип')
    def __str__(self):
        return f'{self.pk}. {self.title}'

class Task(models.Model):
    summary = models.CharField(max_length=50, null=False, blank=False, verbose_name="summary")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="description")
    status = models.ForeignKey('webapp.Status', related_name='tasks',  on_delete=models.PROTECT)
    type = models.ForeignKey('webapp.Type', max_length=20, related_name='tasks', on_delete=models.PROTECT)


    def __str__(self):
        return f'{self.pk}. {self.summary}'


