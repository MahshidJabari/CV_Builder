from django.db import models


class BaseModel(models.Model):
    """Base abstract model to handle all common fields for are models"""
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
