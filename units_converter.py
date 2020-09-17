mera1 = input('Введите исходные единицы измерения из списка доступных(аршин, шаг, верста, сажень, пядь:\n')
number = float(input('Введите число:\n'))
mera2 = input('Введите конечные единицы измерения из списка доступных (м, см):\n')
if mera2 == "см":
    if mera1 == "аршин":
        output = number * 0.7112 * 100
        print(round(output, 4))
    if mera1 == "шаг":
        output = number * 0.71 * 100
        print(round(output, 4))
    if mera1 == "верста":
        output = number * 1066.8 * 100
        print(round(output, 4))
    if mera1 == "сажень":
        output = number * 1.514 * 100
        print(round(output, 4))
    if mera1 == "пядь":
        output = number * 0.1778 * 100
        print(round(output, 4))
else:
    if mera1 == "аршин":
        output = number * 0.7112
        print(round(output, 4))
    if mera1 == "шаг":
        output = number * 0.71
        print(round(output, 4))
    if mera1 == "верста":
        output = number * 1066.8
        print(round(output, 4))
    if mera1 == "сажень":
        output = number * 1.514
        print(round(output, 4))
    if mera1 == "пядь":
        output = number * 0.1778
        print(round(output, 4))
