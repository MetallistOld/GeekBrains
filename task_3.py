tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def gen_corteg():
    index_tutors = 0
    index_klasses = 0
    while index_tutors < len(tutors):
        if index_tutors >= len(klasses):
            yield (tutors[index_tutors], None)
            index_tutors += 1
            index_klasses += 1
        else:
            yield (tutors[index_tutors], klasses[index_klasses])
            index_tutors += 1
            index_klasses += 1


for gen in gen_corteg():
    print(gen)

print(next(gen))
