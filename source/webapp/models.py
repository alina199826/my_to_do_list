from django.db import models
from django.utils import timezone

# Create your models here.

STATUS = [('new', 'новая'), ('moderated', 'модерированная'), ('rejected', 'откланенная')]

class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    author = models.CharField(max_length=50, verbose_name="Автор", default="Unknown")
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    deadline = models.DateField(verbose_name="deadline")
    status = models.CharField(max_length=20, choices=STATUS, default=STATUS[0][0], verbose_name="Статус")
    def __str__(self):
        return f'{self.pk}. {self.title}'
from django.db import models

# Create your models here.
