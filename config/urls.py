from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('control-panel/', admin.site.urls),
    path('payment/', include('apps.payment.urls')),
]
