from django.contrib import admin

from .models import Task


# Register your models here.
@admin.register(Task)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'slug',
        'description',
        'done',
        'created_at',
        'comple_before',
        'updated_at',
    ]
    prepopulated_fields = {'slug': ['name']}
