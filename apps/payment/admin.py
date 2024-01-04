from django.contrib import admin

from apps.payment.models import Transaction

admin.site.register(Transaction)
