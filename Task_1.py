translate_dict = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
                  'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate_adv(translate_number):
    if translate_number[0].isupper():
        upper_chek = True
    else:
        upper_chek = False
    if translate_number.lower() in translate_dict and upper_chek:
        return translate_dict[translate_number.lower()].capitalize()
    elif translate_number in translate_dict and not upper_chek:
        return translate_dict[translate_number]
    else:
        return None


number = input('Введите число: ')
translate = num_translate_adv(number)
print(translate)
