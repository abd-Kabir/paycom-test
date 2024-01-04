from django.urls import path

from apps.payment.views import PaycomMerchantAPI

urlpatterns = [
    path('merchant-api/', PaycomMerchantAPI.as_view(), name='merchant_api')
]
