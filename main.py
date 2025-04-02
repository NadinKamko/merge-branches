def make_meme(text: str) -> str:
    return text.upper().replace('.', '!') + '!' * 3
print(make_meme('Я устал')) # вывод: 'Я УСТАЛ!!!'
print(make_meme('хочу пиццу')) # вывод: 'ХОЧУ ПИЦЦУ!!!'


def make_meme(text: str) -> str:
    return text.upper().translate(str.maketrans({'A':'@', 'S':'$', 'I':'!', 'O':'&'})) + '!!!'
print(make_meme('hello world!!!')) #вывод: HELL& W&RLD!!!
print(make_meme('python is cool')) #вывод: PYTH&N !$ C&&L!!!

