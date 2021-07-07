import os

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}  # Ключ - папка, значение - под папки

for i in starter: # Перебираем ключи словаря
    if not os.path.isdir(i):
        os.mkdir(i)
    else:
        print(f'Пака {i} существует')
    for n in starter[i]:
        if not os.path.isdir(i + '/' + n):
            os.mkdir(i + '/' + n)
        else:
            print(f'Пака {n} существует')
