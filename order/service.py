from abc import ABCMeta, abstractmethod, ABC
from math import sqrt


class DeliveryServices(metaclass=ABCMeta):

    @abstractmethod
    def distance_beetween_points(self):
        pass

    @abstractmethod
    def calc_delivery_price(self):
        pass

    def count_manhattan_distance(self, a, b):
        return sum(abs(val1 - val2) for val1, val2 in zip(a, b))


class YandexService(DeliveryServices):

    def distance_beetween_points(self):
        points = self.get_points()
        x1 = int(points[0])
        y1 = int(points[1])
        x2 = int(points[2])
        y2 = int(points[3])
        A = [x1, y1]
        B = [x2, y2]
        distance = self.count_manhattan_distance(A, B)
        true_distance = distance / 1000
        return true_distance

    def calc_delivery_price(self):
        distance = self.distance_beetween_points()
        if distance <= 10:
            price = 200
        elif 10 < distance <= 100:
            price = 1000
        else:
            price = 2000
        return price

    def get_points(self, ):
        points = {}
        with open("points.txt") as file:
            for line in file:
                key, *value = line.split()
                points[key] = value
        points1 = points.get('Yandex')
        points2 = points.get('My_point')
        points3 = points1 + points2
        return points3

# C:/Users/nik12/Desktop/Django-respect-main/order/


class CourierService(DeliveryServices):

    def distance_beetween_points(self):
        points = self.get_points()
        a = len(points)
        if a == 5:
            address = points[4]
            return address
        elif a == 6:
            address = points[4] + ' ' + points[5]
            return address
        else:
            address = ''
            return address

    def calc_delivery_price(self):
        address = self.distance_beetween_points()
        if address == '':
            return 'Укажите город для доставки'
        elif address == 'Moscow' or address == 'Saint Petersburg':
            price = 700
            return price
        else:
            return 'В ваш город не осуществляется доставка'

    def get_points(self, ):
        points = {}
        with open("points.txt") as file:
            for line in file:
                key, *value = line.split()
                points[key] = value
        points1 = points.get('Courier')
        points2 = points.get('My_point')
        points3 = points1 + points2
        return points3


class SDEKService(DeliveryServices):
    def distance_beetween_points(self):
        points = self.get_points()
        x1 = int(points[0])
        y1 = int(points[1])
        x2 = int(points[2])
        y2 = int(points[3])
        dist = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        true_distance = dist / 1000
        return true_distance

    def calc_delivery_price(self):
        distance = self.distance_beetween_points()
        if distance <= 10:
            price = 100
        elif 10 < distance <= 25:
            price = 250
        else:
            price = 1000
        return price

    def get_points(self, ):
        points = {}
        with open("points.txt") as file:
            for line in file:
                key, *value = line.split()
                points[key] = value
        points1 = points.get('SDEK')
        points2 = points.get('My_point')
        points3 = points1 + points2
        return points3


class DeliveryType(str):
    YANDEX = 'Yandex'
    SDEK = 'SDEK'
    COURIER = 'Courier'

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
