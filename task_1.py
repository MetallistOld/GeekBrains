from time import sleep


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i != 3:
            print(f'На светофоре горит {TrafficLight.__color[i]} свет')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(5)
            if i == 2:
                i = 0
            else:
                i += 1


t = TrafficLight()
t.running()
