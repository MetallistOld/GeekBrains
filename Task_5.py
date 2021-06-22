from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(number_joke, flag):
    for _ in range(number_joke):
        first_word = choice(nouns)
        second_word = choice(adverbs)
        third_word = choice(adjectives)
        joke = f'{first_word} {second_word} {third_word}'
        if flag:
            nouns.remove(first_word)
            adverbs.remove(second_word)
            adjectives.remove(third_word)
        print(joke)


index = int(input('Введите количество шуток (1-5): '))
get_jokes(index, True)
