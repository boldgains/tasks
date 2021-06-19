from django.contrib import admin

from todos.models import Todo
# Register your models here.


@admin.register(Todo)
class TodosAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'is_complete',
        'date_completed'
    ]
