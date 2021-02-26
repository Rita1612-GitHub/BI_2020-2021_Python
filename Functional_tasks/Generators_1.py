# Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n (аккуратно, не
# вызывайте её с n > 8)
# Пример вызова
# list(generate(2))
# ['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC', 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

import itertools

n = int(input())
def generate(n):
    for i in range(1, n+1):
        l = itertools.product(["A", "T", "G", "C"], repeat = i)
        for j in l:
            yield "".join(j)

print(list(generate(n)))
