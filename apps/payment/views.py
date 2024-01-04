import logging

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.payment.serializer import PaymeMerchantAPISerializer
from apps.payment.utils.services import paycom_services

logger = logging.getLogger()


class PaycomMerchantAPI(APIView):
    def post(self, request, *args, **kwargs):
        logger.debug(f"Data: {request.data}; Params: {request.query_params}")

        serializer = PaymeMerchantAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        method = serializer.data['method']
        params = serializer.data['params']

        response = paycom_services[method](params)
        return Response(response)
