import os

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=255)
    category_id = models.IntegerField()

class Catalog(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category,
        models.CASCADE,
        verbose_name=('category_id'),
    )
    description = models.TextField()
    create_date = models.DateTimeField(null=True)
    delete_date = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(
        User,
        models.CASCADE,
        verbose_name=('user_id'),
    )


