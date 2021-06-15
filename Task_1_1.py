seconds = int(input('duration= '))
if seconds < 60: # Проверяем, если меньше 60 секунд (1 минуты) выводим само значение
    print(seconds,' сек')
elif seconds < 3600: # Проверяем, если меньше 3600 секунд (1 час)
    minutes = seconds // 60
    seconds = seconds % 60
    print("{} мин {} сек".format(minutes, seconds))
elif seconds < 86400: # Проверяем, если меньше 86400 секунд (1 день)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print("{} час {} мин {} сек".format(hours, minutes, seconds))
elif seconds < 2678400: # Проверяем, если меньше 2678400 секунд (1 месяц)
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print("{} дн {} час {} мин {} сек".format(days, hours, minutes, seconds))
elif seconds < 32140800: # Проверяем, если меньше 32140800 секунд (1 год)
    month = seconds // 2678400
    days = (seconds % 2678400) // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print("{} мес {} дн {} час {} мин {} сек".format(month, days, hours, minutes, seconds))
else:
    years = seconds // 32140800 #В остальных случаях больше года
    month = (seconds % 32140800) // 2678400
    days = (seconds % 2678400) // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    print("{} год {} мес {} дн {} час {} мин {} сек".format(years, month, days, hours, minutes, seconds))
