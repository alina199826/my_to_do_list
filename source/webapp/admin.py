from django.contrib import admin

from webapp.models import Task

# Register your models here


class TackAdmin(admin.ModelAdmin):
     list_display = ['id',  'summary', 'status', 'type', 'updated_at', 'created_at']
     list_filter = ['status']
     search_fields = ['summary']
     exclude = []

admin.site.register(Task, TackAdmin)