import enum
from order.service import YandexService, SDEKService, CourierService


@enum.unique
class DeliveryType(str, enum.Enum):
    YANDEX = 'YANDEX'
    SDEK = 'SDEK'
    COURIER = 'COURIER'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


def count_price_for_delivery(delivery_type):
    if delivery_type == DeliveryType.YANDEX:
        yandex_service = YandexService()
        result = yandex_service.calc_delivery_price()
        return result
    elif delivery_type == DeliveryType.SDEK:
        sdek_service = SDEKService()
        result = sdek_service.calc_delivery_price()
        return result
    else:
        courier_service = CourierService()
        result = courier_service.calc_delivery_price()
        return result
