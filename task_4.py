import os

folder = 'some_data'

res = {}
size_start = 0
size_end = 100 * 2 ** 10
size_count = 100

while True:
    size_files = [item.name
                  for item in os.scandir(folder)
                  if size_start < item.stat().st_size < size_end]

    if len(size_files) == 0:
        break
    res[size_count] = len(size_files)

    size_start = size_end
    size_end = size_start * 10
    size_count = size_count * 10
print(res)
