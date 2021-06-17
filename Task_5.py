# Создать список, содержащий цены на товары (10–20 товаров), например:
# [57.8, 46.51, 97, ...]
# * Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).
#
# * Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
# * Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
price_item = [57.8, 46.51, 97, 55.4, 12.3, 78.54, 77.3, 33, 44, 45.12, 90.90, 12.1, 1.3, 22.2]
print('ID Списка: ', id(price_item))
stroka_prices = ''
for res in price_item:
    price = str(res).split('.')
    if len(price) > 1:
        rubl = int(price[0])
        coins = int(price[1])
    else:
        rubl = int(price[0])
        coins = 0
    stroka_prices += f'{rubl} руб. {coins:02d} коп., '
stroka_prices = stroka_prices[:-2]
print(stroka_prices)

price_item.sort()

stroka_prices = ''
for res in price_item:
    price = str(res).split('.')
    if len(price) > 1:
        rubl = int(price[0])
        coins = int(price[1])
    else:
        rubl = int(price[0])
        coins = 0
    stroka_prices += f'{rubl} руб. {coins:02d} коп., '
stroka_prices = stroka_prices[:-2]
print(stroka_prices)
print('ID Списка: ', id(price_item))