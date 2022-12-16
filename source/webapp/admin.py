from django.contrib import admin

from webapp.models import Task, Status, Type, Project
# Register your models here


class TackAdmin(admin.ModelAdmin):
     list_display = ['id',  'summary', 'status', 'updated_at', 'created_at']
     list_filter = ['status']
     search_fields = ['summary']
     exclude = []


class ProjectAdmin(admin.ModelAdmin):
     list_display = ['title', 'content', 'date_start', 'date_end']
     exclude = []

admin.site.register(Task, TackAdmin)
admin.site.register(Status)
admin.site.register(Type)

admin.site.register(Project, ProjectAdmin)