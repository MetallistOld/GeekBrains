translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}  # Словарь создаем


# глобальным, что бы не пересозавать его каждый раз при вызове функции


def num_translate_adv(translate_number):
    if translate_number[0].isupper():  # Проверяем первую букву, заглавная или нет
        upper_check = True
    else:
        upper_check = False
    if translate_number.lower() in translate_dict and upper_check:
        return translate_dict[
            translate_number.lower()].capitalize()  # Если первая буква заглавная, возвращаем результат с заглавной буквы
    elif translate_number in translate_dict and not upper_check:
        return translate_dict[
            translate_number]  # Если первая буква не заглавная, возвращаем результат с маленокой буквы
    else:
        return None  # Если запрашиваемого числа нет в словаре, возвращаем None


number = input('Введите число: ')
print(num_translate_adv(number))
