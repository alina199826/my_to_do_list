# Generated by Django 4.1.4 on 2022-12-27 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_alter_project_users'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'permissions': [('сan_see_list_user', 'Может смотреть профили пользователей')]},
        ),
    ]