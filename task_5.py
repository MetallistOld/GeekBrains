src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

unique_brands = []
tmp = []
for el in src:
    if el not in tmp:
        unique_brands.append(el)
    elif el in unique_brands:
        unique_brands.pop(unique_brands.index(el))
    tmp.append(el)
print(unique_brands)