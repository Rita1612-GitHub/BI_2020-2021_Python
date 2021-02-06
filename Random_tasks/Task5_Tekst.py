import re
from random import shuffle

template = re.compile(r"\b(\w)(\w+)(\w)\b")  # шаблон для отбора слов в строке


def shuffle_word(match):
    first, middle, last = match.groups()  # отобрали первую букву, середину и последнюю букву
    middle = list(middle)  # перевели в лист
    shuffle(middle)  # перемешали случайным образом
    return first + ''.join(middle) + last  # обратно соединили


def get(sentence):
    return template.sub(shuffle_word, sentence)  # отбор регекспом по шаблону, применение к нему функции shuffle_word


x = '\n'.join(iter(input, 'stop'))  # текст считывается, пока не будет слово stop
print('\n' + get(x))  # печать результата
