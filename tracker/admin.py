from django.contrib import admin
from tracker.models import Performer, Project, Task


@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'removed_tasks_count')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'performer', 'priority', 'created_date', 'deadline', 'comment')
