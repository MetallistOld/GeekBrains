from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def consumption(self):
        pass

    def __add__(self, other):
        return self.consumption + other.consumption

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def consumption(self):
        return round(self.param / 6.5) + 0.5


class Costume(Clothes):

    @property
    def consumption(self):
        return 2 * self.param + 0.3


coat = Coat(400)
costume = Costume(55)
print(f'Для пошива пальто нужно: {coat.consumption} ткани')
print(f'Для пошива костюма нужно: {costume.consumption} ткани')
print(f'Всего нужно {coat + costume} ткани')
