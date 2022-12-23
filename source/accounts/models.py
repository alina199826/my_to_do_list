from django.db import models

class Profile(models.Model):
    biography = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Дата Роджения')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar', verbose_name='Фото')
