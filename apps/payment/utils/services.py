from datetime import datetime
from random import randint

from .methods import (CHECK_PERFORM_TRANSACTION, CREATE_TRANSACTION,
                      PERFORM_TRANSACTION, CANCEL_TRANSACTION,
                      CHECK_TRANSACTION)


def check_perform_transaction(params) -> dict:
    return {
        "result": {
            "allow": True
        }
    }


def create_transaction(params) -> dict:
    transaction_id = randint(100_000, 999_999)
    create_time = datetime.now().timestamp()
    return {
        "result": {
            "create_time": create_time,
            "transaction": transaction_id,
            "state": 1
        }
    }


def perform_transaction(params) -> dict:
    transaction_id = randint(100_000, 999_999)
    perform_time = datetime.now().timestamp()
    return {
        "result": {
            "perform_time": perform_time,
            "transaction": transaction_id,
            "state": 2
        }
    }


def cancel_transaction(params) -> dict:
    transaction_id = randint(100_000, 999_999)
    cancel_time = datetime.now().timestamp()
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
            "create_time": datetime.now().timestamp(),
            "perform_time": datetime.now().timestamp(),
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
