from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField('model created at', null=True, auto_now_add=True)
    updated_at = models.DateTimeField('model updated at', null=True, auto_now_add=True)

    class Meta:
        abstract = True
