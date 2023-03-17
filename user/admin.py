from django.contrib import admin
from user.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass

