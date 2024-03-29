# Generated by Django 4.1.3 on 2022-11-07 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_task_delete_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
    ]
