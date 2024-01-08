from django.contrib import admin
from apps.payment.models import Transaction, Package

admin.site.register(Package)
admin.site.register(Transaction)
