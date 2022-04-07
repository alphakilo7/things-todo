from django.conf import settings
from django.db import models


class TimestampMixin(models.Model):
    """An abstract model to log creation and updation of models"""
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TodoList(TimestampMixin, models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name="todo_lists", blank=True, null=True)

    def __str__(self):
        return self.title


class Task(TimestampMixin, models.Model):
    TASK_STATUSES = [
        ("TODO", "TODO"),
        ("IN_PROGRESS", "In Progress"),
        ("DONE", "Done"),
    ]
    todo_list = models.ForeignKey(
        "todo.TodoList", on_delete=models.CASCADE, related_name="items")

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=TASK_STATUSES, default="TODO")
    due_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{}-{}".format(self.title, self.status)
