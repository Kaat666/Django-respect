from abc import ABCMeta, abstractmethod, ABC
from math import sqrt


class DeliveryServices(metaclass=ABCMeta):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def distance_beetween_points(self, address, x_user, y_user) -> float:
        pass

    @abstractmethod
    def calc_delivery_price(self, address, x_user, y_user) -> int:
        pass

    def count_manhattan_distance(self, a, b):
        return sum(abs(val1 - val2) for val1, val2 in zip(a, b))

    def get_points(self, x_user, y_user):
        points = GetPoints.from_file("points.txt")
        A = [x_user, y_user]
        B = [points[0], points[1]]
        C = [points[2], points[3]]
        distance = self.count_manhattan_distance(A, B)
        another_distance = self.count_manhattan_distance(A, C)
        if distance >= another_distance:
            return A + C
        else:
            return A + B


class MyException(Exception):
    print ('Укажите город доставки')


class MyException1(Exception):
    print('На указанный адрес доставка не осуществляется')


class YandexService(DeliveryServices):
    def distance_beetween_points(self, address, x_user, y_user):
        points = self.get_points(x_user, y_user)
        A = [points[0], points[1]]
        B = [points[2], points[3]]
        distance = self.count_manhattan_distance(A, B)
        true_distance = distance / 1000
        return true_distance

    def calc_delivery_price(self, address, x_user, y_user):
        distance = self.distance_beetween_points(address, x_user, y_user)
        if distance <= 10:
            price = 200
        elif 10 < distance <= 100:
            price = 1000
        else:
            price = 2000
        return price


class CourierService(DeliveryServices):

    def distance_beetween_points(self, address, x_user, y_user):
        return address

    def calc_delivery_price(self, address, x_user, y_user) -> int:
        address = self.distance_beetween_points(address, x_user, y_user)
        if address == '':
            raise MyException(Exception)
        elif 'Moscow' in address or 'Saint Petersburg' in address:
            price = 700
            return price
        else:
            raise MyException1(Exception)


class SDEKService(DeliveryServices):
    def distance_beetween_points(self, address, x_user, y_user):
        points = self.get_points(x_user, y_user)
        A = [points[0], points[1]]
        B = [points[2], points[3]]
        distance = self.count_manhattan_distance(A, B)
        true_distance = distance / 1000
        return true_distance

    def calc_delivery_price(self, address, x_user, y_user):
        distance = self.distance_beetween_points(address, x_user, y_user)
        if distance <= 10:
            price = 100
        elif 10 < distance <= 25:
            price = 250
        else:
            price = 1000
        return price


class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x)
        print(self.y)


class GetPoints:

    @staticmethod
    def from_file(filepath: str):
        with open(filepath) as f:
            points = {line.split()[0]: [int(j) for j in line.split()[1:]] for line in f}
            points1 = points.get('Yandex')
            return points1

    def get_point():
        points = []
        with open("points.txt") as file:
            for line in file:
                key, x, y = line.split()
                if key == "Yandex":
                    points.append(Point(int(x), int(y)))
        print(points)
        return points


class DeliveryType(str):
    YANDEX = 'Yandex'
    SDEK = 'SDEK'
    COURIER = 'Courier'

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


# delivery_factory( delivery_type)


def delivery_factory(delivery_type):
    if delivery_type == DeliveryType.YANDEX:
        return YandexService(delivery_type)
    elif delivery_type == DeliveryType.SDEK:
        return SDEKService(delivery_type)
    else:
        CourierService(delivery_type)
        return CourierService(delivery_type)


bebe = GetPoints
print(bebe.get_point())

# bibi = YandexService('Yandex')
# print(bibi.calc_delivery_price('Moscow', 1500, 3000))
