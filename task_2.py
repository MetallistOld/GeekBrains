"""Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой. """


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div():
    try:
        user_number_1 = int(input('Введите делимое: '))
        user_number_2 = int(input('Введите делитель: '))
        if user_number_2 == 0:
            raise OwnError("Делить на ноль нельзя!")
        else:
            res = user_number_1 / user_number_2
            return res
    except ValueError:
        return "Вы ввели не число"
    except OwnError as err:
        return err


print(div())
