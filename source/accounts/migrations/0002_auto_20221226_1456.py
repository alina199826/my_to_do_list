


from django.db import migrations


def create_profiles(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Profile = apps.get_model('accounts', 'Profile')
    users = User.objects.filter(profile__isnull=True)
    for user in users:
        Profile.objects.get_or_create(user=user)


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0001_initial'),

    ]

    operations = [
        migrations.RunPython(create_profiles, migrations.RunPython.noop)
    ]
