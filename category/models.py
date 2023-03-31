from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=100)
