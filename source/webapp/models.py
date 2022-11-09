from django.db import models


# Create your models here.

STATUS = [('new', 'новая'), ('moderated', 'модерированная'), ('rejected', 'откланенная')]


class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="title")
    deadline = models.DateField(verbose_name="deadline")
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0], verbose_name="status")
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="description")

    def __str__(self):
        return f'{self.pk}. {self.title}'


