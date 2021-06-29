number = int(input('Введите число: '))


# Вариант генератора с yield
def nums_generator(count):
    for num in range(1, count + 1, 2):
        yield num


def IterationPrint(generation): # Вывод результата работы генератора, до возникновения ошибки StopIteration
    while True:
        try:
            print(next(nums_gen))
        except StopIteration:
            print('...StopIteration...')
            break


nums_gen = nums_generator(number)

IterationPrint(nums_gen)

# Вариант генератора без yield
nums_gen = (num for num in range(1, number + 1, 2))

IterationPrint(nums_gen)
