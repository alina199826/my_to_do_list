# Generated by Django 4.1.3 on 2022-11-21 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_remove_task_type_task_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.status'),
        ),
    ]
