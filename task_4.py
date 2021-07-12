class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f'Полицейская машина {self.name} преследует нарушителя'
        else:
            return f'Машина {self.name} поехала'

    def stop(self):
        return f'\nМашина {self.name} остановилась'

    def turn(self, direction):
        return f'\nМашина {self.name} повернула {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля "{self.name}" - "{self.speed}" км/ч.'


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'\nМашина {self.name} нарушает и двигается со скоростью {self.speed}'
        else:
            return f'\nМашина {self.name} не превышает разрешенную скорость'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nМашина {self.name} нарушает и двигается со скоростью {self.speed}'
        else:
            return f'\nМашина {self.name} не превышает разрешенную скорость'


class PoliceCar(Car):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)
        self.is_police = True


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())

work = WorkCar('VAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('BMV', 100, 'yellow', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())
