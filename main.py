def make_meme(text: str) -> str:
    return text.upper().replace('.', '!') + '!' * 3
print(make_meme('Я устал')) # вывод: 'Я УСТАЛ!!!'
print(make_meme('хочу пиццу')) # вывод: 'ХОЧУ ПИЦЦУ!!!'


