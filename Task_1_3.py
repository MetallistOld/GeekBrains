number = int(input('Введите число от 1 до 20: '))

if number == 1:
    print(number, 'процент')
elif number >= 2 and number <=4:
    print(number, 'процента')
else:
    print(number, 'процентов')
for x in range(1, 21):
    if x == 1:
        print(x, 'процент')
    elif x >= 2 and x <=4:
        print(x, 'процента')
    else:
        print(x, 'процентов')