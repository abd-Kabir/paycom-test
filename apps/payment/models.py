import uuid

from django.contrib.auth.models import User
from django.db import models
from config.models import BaseModel


class Package(BaseModel):
    name = models.CharField(max_length=55)
    amount = models.PositiveIntegerField()

    class Meta:
        db_table = 'Package'


class Transaction(BaseModel):
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILED = 'failed'
    CANCELED = 'canceled'
    STATUS = (
        (PROCESSING, 'processing'),
        (SUCCESS, 'success'),
        (FAILED, 'failed'),
        (CANCELED, 'canceled')
    )
    status = models.CharField(choices=STATUS, default='processing', max_length=55)
    payment_id = models.CharField(max_length=255, null=True, blank=True)
    transaction_key = models.CharField(max_length=255, null=True, blank=True)
    state = models.IntegerField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    create_datetime = models.DateTimeField(null=True, blank=True)
    perform_datetime = models.DateTimeField(null=True, blank=True)
    cancel_datetime = models.DateTimeField(null=True, blank=True)
    reason = models.IntegerField(blank=True, null=True)

    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.payment_id}"

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.payment_id:
            self.payment_id = uuid.uuid4().hex
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'Transaction'
