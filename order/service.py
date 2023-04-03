import dataclasses
from abc import ABCMeta, abstractmethod
import json


@dataclasses.dataclass
class Point:
    x: int
    y: int
    delivery_type: str


class DeliveryType(str):
    YANDEX = 'Yandex'
    SDEK = 'SDEK'
    COURIER = 'Courier'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


class DeliveryServices(metaclass=ABCMeta):
    DELIVERY_TYPE = None

    @abstractmethod
    def calc_delivery_price(self, address, x_user, y_user) -> int:
        pass

    def count_manhattan_distance(self, a, b):
        return sum(abs(val1 - val2) for val1, val2 in zip(a, b))

    @classmethod
    def get_points(cls):
        points = []
        with open("points.json") as file:
            file_points = json.load(file)["points"]
            for point in file_points:
                if point["delivery_type"] == cls.DELIVERY_TYPE:
                    points.append(Point(x=point["x"], y=point["y"], delivery_type=point["delivery_type"]))
        return points

    def distance_between_points(self, x_user: int, y_user: int) -> float:
        points = self.get_points()
        if not points:
            raise AttributeError("Укажите коррдинаты доставки")
        user_point = [x_user, y_user]
        first_point = [points[0].x, points[0].y]
        minimum = self.count_manhattan_distance(user_point, first_point)
        for point in points[1:]:
            current_point = [point.x, point.y]
            distance = self.count_manhattan_distance(user_point, current_point)
            minimum = min(minimum, distance)

        return minimum


class YandexService(DeliveryServices):
    DELIVERY_TYPE = DeliveryType.YANDEX

    def calc_delivery_price(self, address, x_user, y_user):
        distance = self.distance_between_points(x_user, y_user)
        if distance <= 10:
            price = 200
        elif 10 < distance <= 100:
            price = 1000
        else:
            price = 2000
        return price


class CourierService(DeliveryServices):
    DELIVERY_TYPE = DeliveryType.COURIER

    def calc_delivery_price(self, address, x_user, y_user) -> int:
        if address == '':
            raise AttributeError('Укажите адрес доставки')
        elif 'Moscow' in address or 'Saint Petersburg' in address:
            price = 700
            return price
        else:
            raise AttributeError(
                'На указанный адрес доставка не осуществляется(Мы доставляем только в Moscow и Saint Petersburg)')


class SDEKService(DeliveryServices):
    DELIVERY_TYPE = DeliveryType.SDEK

    def calc_delivery_price(self, address, x_user, y_user):
        distance = self.distance_between_points(x_user, y_user)
        if distance <= 10:
            price = 100
        elif 10 < distance <= 25:
            price = 250
        else:
            price = 1000
        return price


def delivery_factory(delivery_type):
    if delivery_type == DeliveryType.YANDEX:
        return YandexService()
    elif delivery_type == DeliveryType.SDEK:
        return SDEKService()
    else:
        return CourierService()
