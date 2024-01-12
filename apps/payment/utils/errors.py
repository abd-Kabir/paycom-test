PROCESSING = 'processing_er'
NOT_FOUND = 'not_found_er'
BLOCKED = 'blocked_er'
AMOUNT = 'amount_er'

payment_errors = {
    PROCESSING: {
        "code": -31008,
        "message": {
            "uz": "Buyurtma amalga oshirilmoqda",
            "ru": "Заказ в процессе обработки",
            "en": "Order payment in process"
        }
    },
    NOT_FOUND: {
        "code": -31003,
        "message": {
            "uz": 'Buyurtma topilmadi',
            "ru": 'Транзакция не найдена',
            "en": 'Transaction not found'
        }
    },
    BLOCKED: {
        "code": -31008,
        "message": {
            "uz": "Hisob to'langan/bekor qilingan",
            "ru": 'Счет уже оплачен / отменен',
            "en": 'Invoice already paid/cancelled'
        }
    },
    AMOUNT: {
        "code": -31001,
        "message": {
            "uz": "Noto'g'ri summa",
            "ru": 'Неверная сумма',
            "en": 'Incorrect amount'
        }
    }
}
