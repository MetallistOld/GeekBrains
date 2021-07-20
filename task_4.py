# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

class Sklad:

    def __init__(self, name):
        self.name = name

class Orgtehnika:

    def __init__(self, brand, color):
        self.Brand = brand
        self.Color = color

    def __str__(self):
        return f"Brand and Color: {self.Brand} {self.Color}"

class Printer(Orgtehnika):

    def __init__(self, brand, color, type):
        super().__init__(brand, color)
        self.type = type

class Skaner(Orgtehnika):

    def __init__(self, brand, color, size):
        super().__init__(brand, color)
        self.size = size

class Kserox(Orgtehnika):

    def __init__(self, brand, color, is_professional):
        super().__init__(brand, color)
        self.is_professional = is_professional

my_item1 = Printer('Epson', 'Белый', 'лазерный')
print(my_item1)
my_item2 = Skaner('HP', 'Чёрный', 'А4')
print(my_item2)
my_item3 = Kserox('Майкрософт', 'Чёрный', True)
print(my_item3)

my_sklad = Sklad('Мой склад')
print(my_sklad.name)
