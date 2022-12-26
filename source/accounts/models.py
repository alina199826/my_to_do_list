from django.contrib.auth import get_user_model
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE,
                                verbose_name='Пользователь')
    biography = models.TextField(max_length=1000, null=True, blank=True, verbose_name='Биография')
    avatar = models.ImageField(null=True, blank=True, upload_to='user_avatar', verbose_name='Фото')
    link = models.URLField(max_length=200, null=True, blank=True, verbose_name='Cсылка')



    def __str__(self):
        return f"{self.user}"


    class Meta:
        db_table = 'profile'
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'