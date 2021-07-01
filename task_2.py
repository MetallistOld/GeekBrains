import collections
from time import perf_counter
result = []
with open('nginx_logs.txt', 'r') as f:
    for x in f:
        result.append(x.split()[0])
start = perf_counter()
res = collections.Counter()
for word in result:
    res[word] += 1
result_spam = res.most_common(1)
print(f'Спам с IP : {result_spam[0][0]} : {result_spam[0][1]} раз')
print('Поиск IP спамера :', perf_counter() - start)
