from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


@admin.register(User)
class TodoUserAdmin(UserAdmin):
    list_display = ["id", "username", "email", "date_joined"]
