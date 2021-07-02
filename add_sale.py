from sys import argv

if len(argv) == 1:
    print('Необходимо добавить сумму продаж. Пример: "add_sale.py 55,78"')
elif len(argv) == 2:
    with open('bakery.csv', 'a') as f:
        f.write(argv[1] + '\n')
    print(f'сумма продаж {argv[1]} добавлена')
else:
    print('Слишком много параметров')
