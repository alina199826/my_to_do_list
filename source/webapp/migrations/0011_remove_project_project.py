# Generated by Django 4.1.3 on 2022-12-05 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_alter_task_summary_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='project',
        ),
    ]