"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать
число, месяц, год и преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить
валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных
данных."""

from datetime import date

class Data:
    def __init__(self, date):
        self.data = date

    @classmethod
    def date(cls,date):
        try:
            day, month, year = [int(i) for i in date.split('-')]
            return f"{day}\n{month}\n{year}"
        except ValueError:
            return f'Указана дата: {date} - неправильная !'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return f'Дата {day:2}.{month:2}.{year:4} корректная'
        except ValueError:
            return f'Указана дата: {data} - неправильная !'


print(Data.valid('20-07-2021'))
print(Data.valid('20-07'))
print(Data.date('20-07-2021'))
print(Data.date('20-07'))
