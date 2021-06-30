# Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
# [
#     ...
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('141.138.90.60', 'GET', '/downloads/product_2'),
#     ('173.255.199.22', 'GET', '/downloads/product_2'),
#     ...
# ]


result = []
with open('nginx_logs.txt', 'r') as f:
    for x in f:
        data = f.readline().split()
        add_tuple = (data[0], data[5][1:], data[6])  # выбираем нужные элементы списка
        result.append(add_tuple)  # добавляем кортежи в список

for x in range(5):  # вывод часть списка для проверки правильности его заполнения
    print(result[x])
