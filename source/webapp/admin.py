from django.contrib import admin

from webapp.models import Task, Status, Type
# Register your models here


class TackAdmin(admin.ModelAdmin):
     list_display = ['id',  'summary', 'status', 'updated_at', 'created_at']
     list_filter = ['status']
     search_fields = ['summary']
     exclude = []

admin.site.register(Task, TackAdmin)
admin.site.register(Status)
admin.site.register(Type)