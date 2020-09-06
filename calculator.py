a = int(input())
b = str(input())
c = int(input())
if b == '+': d=a+c
if b == "-": d=a-c
if b == "*": d=a*c
if (b == "/") and (c==0):
    print('Деление на ноль!')
if b == "/": d=a/c
print(d)
