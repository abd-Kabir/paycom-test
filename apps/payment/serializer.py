from rest_framework import serializers

from utils.methods import METHODS


class PaymeMerchantAPISerializer(serializers.Serializer):
    method = serializers.ChoiceField(choices=METHODS, required=False)
    params = serializers.JSONField(required=False)
