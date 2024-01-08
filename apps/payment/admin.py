from django.contrib import admin
from django.contrib.auth.models import User

from apps.payment.models import Transaction, Package

admin.site.register(User)
admin.site.register(Package)
admin.site.register(Transaction)
