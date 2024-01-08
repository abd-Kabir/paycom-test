from datetime import datetime
from random import randint

from .methods import (CHECK_PERFORM_TRANSACTION, CREATE_TRANSACTION,
                      PERFORM_TRANSACTION, CANCEL_TRANSACTION,
                      CHECK_TRANSACTION)
from ..models import Transaction


def check_perform_transaction(params) -> dict:
    return {
        "result": {
            "allow": True
        }
    }


def create_transaction(params) -> dict:
    create_datetime = datetime.now()
    amount = params.get('amount')
    transaction_key = params.get('id')
    if transaction_key in Transaction.objects.values_list('transaction_key', flat=True):
        instance = Transaction.objects.filter(transaction_key=transaction_key).first()
    else:
        account_id = params.get('account').get('user')
        package_id = params.get('account').get('Tarif')
        if Transaction.objects.filter(package_id=package_id,
                                      user_id=account_id,
                                      status='processing').exists():
            return {
                "error": {
                    "code": -31099,
                    "message": {
                        "uz": "Buyurtma amalga oshirilmoqda",
                        "ru": "Заказ в процессе обработки",
                        "en": "Order payment in process"
                    }
                }
            }
        instance = Transaction.objects.create(create_datetime=create_datetime,
                                              transaction_key=transaction_key,
                                              amount=amount,
                                              state=1,
                                              status='processing')
    return {
        "result": {
            "create_time": instance.create_datetime.timestamp() * 1000,
            "transaction": instance.payment_id,
            "state": instance.state
        }
    }


def perform_transaction(params) -> dict:
    transaction_id = randint(100_000, 999_999)
    perform_time = int(datetime.now().timestamp() * 1000)
    return {
        "result": {
            "perform_time": perform_time,
            "transaction": transaction_id,
            "state": 2
        }
    }


def cancel_transaction(params) -> dict:
    transaction_id = randint(100_000, 999_999)
    cancel_time = int(datetime.now().timestamp() * 1000)
    return {
        "result": {
            "cancel_time": cancel_time,
            "transaction": transaction_id,
            "state": -2
        }
    }


def check_transaction(params) -> dict:
    transaction_key = params.get('id')
    instance = Transaction.objects.get(transaction_key=transaction_key)
    create_time = instance.create_datetime
    if create_time:
        create_time = create_time.timestamp() * 1000
    perform_time = instance.perform_datetime
    if perform_time:
        perform_time = perform_time.timestamp() * 1000
    cancel_time = instance.cancel_datetime
    if cancel_time:
        cancel_time = cancel_time.timestamp() * 1000

    return {
        "result": {
            "create_time": create_time or 0,
            "perform_time": perform_time or 0,
            "cancel_time": cancel_time or 0,
            "transaction": instance.payment_id,
            "state": instance.state,
            "reason": instance.reason
        }
    }


paycom_services = {
    CHECK_PERFORM_TRANSACTION: check_perform_transaction,
    CREATE_TRANSACTION: create_transaction,
    PERFORM_TRANSACTION: perform_transaction,
    CANCEL_TRANSACTION: cancel_transaction,
    CHECK_TRANSACTION: check_transaction
}
