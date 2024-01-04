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
    create_time = int(create_datetime.timestamp() * 1000)
    amount = params.get('amount')
    order_key = params.get('id')
    instance = Transaction.objects.create(create_datetime=create_datetime,
                                          order_key=order_key,
                                          amount=amount)
    return {
        "result": {
            "create_time": create_time,
            "transaction": instance.payment_id,
            "state": 1
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
    transaction_id = randint(100_000, 999_999)
    return {
        "result": {
            "create_time": int(datetime.now().timestamp() * 1000),
            "perform_time": int(datetime.now().timestamp() * 1000),
            "cancel_time": 0,
            "transaction": transaction_id,
            "state": 2,
            "reason": None
        }
    }


paycom_services = {
    CHECK_PERFORM_TRANSACTION: check_perform_transaction,
    CREATE_TRANSACTION: create_transaction,
    PERFORM_TRANSACTION: perform_transaction,
    CANCEL_TRANSACTION: cancel_transaction,
    CHECK_TRANSACTION: check_transaction
}
