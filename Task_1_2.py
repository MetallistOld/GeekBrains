list_numbers = [x ** 3 for x in range(1, 1001) if x % 2 != 0] # Генерируем список из нечетных чисел от 1 до 1000 возведеннык в куб
result = 0
for x in list_numbers: #Цикл по элементам списка
    summa_number = 0 # Обнуление суммы
    number = x # Текущее обрабатываемое число из списка
    while (number != 0): # Цикл по каждой цифре из числа в списке
        summa_number = summa_number + number % 10 # # Прибавляем младший разряд числа
        number = number // 10 # Отбрасываем младший разряд числа
    if summa_number % 7 == 0: # Проверяем делиться ли сумма чисел на 7 без остатка
        result += x
print(result)
result = 0
for x in list_numbers: #Цикл по элементам списка
    summa_number = 0 # Обнуление суммы
    number_from_spisok = x + 17
    number = x + 17 # Текущее обрабатываемое число из списка
    while (number != 0): # Цикл по каждой цифре из числа в списке
        summa_number = summa_number + number % 10 # # Прибавляем младший разряд числа
        number = number // 10 # Отбрасываем младший разряд числа
    if summa_number % 7 == 0: # Проверяем делиться ли сумма чисел на 7 без остатка
        result += number_from_spisok
print(result)
