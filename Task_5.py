from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n):
    for _ in range(n):
        first_word = choice(nouns)
        second_word = choice(adverbs)
        third_word = choice(adjectives)
        joke = f'{first_word} {second_word} {third_word}'
        print(joke)


index = int(input('Введите количество шуток: '))
get_jokes(index)
