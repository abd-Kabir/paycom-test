from rest_framework import serializers

from apps.payment.utils.methods import METHODS


class PaymeMerchantAPISerializer(serializers.Serializer):
    method = serializers.ChoiceField(choices=METHODS, required=False)
    params = serializers.JSONField(required=False)
