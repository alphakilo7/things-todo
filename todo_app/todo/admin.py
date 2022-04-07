from django.contrib import admin

from todo.models import TodoList, Task


@admin.register(TodoList)
class TodoListAdmin(admin.ModelAdmin):

    list_display = ["title", "owner", "description"]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ["title", "status", "due_date", "todo_list"]
