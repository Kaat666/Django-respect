from django.contrib.auth.models import User
from django.db import models


class Users(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="user", blank=True
    )
