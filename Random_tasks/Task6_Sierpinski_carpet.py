import random
import matplotlib.pyplot as plt


def draw(points):
    xx = [x for (x, y) in points]  # массив x-ов
    yy = [y for (x, y) in points]  # массив y-ов

    figure = plt.figure(figsize=(4, 4), dpi=200)  # размер изображения
    axes = figure.add_subplot()  # добавляет оси на рисунок
    axes.scatter(xx, yy, c='green', s=0.01)
    plt.title('Sierpinski carpet', size=12)  # название рисунка
    plt.xlabel("x")  # подпись оси x
    plt.ylabel("y")  # подпись оси y
    plt.tight_layout(pad=5)
    plt.show()


def calculate(n):  # генерация точек
    vershiny = [(0, 0), (0.5, 0), (1, 0), (1, 0.5), (1, 1), (0.5, 1), (0, 1), (0, 0.5)]
    points = []
    x, y = random.choice(vershiny)  # случайно выбрали одну из вершин для старта

    for i in range(n):  # генерация последующих точек на основе предыдущих
        vx, vy = random.choice(vershiny)
        x = (vx * 2 + x) / 3.0
        y = (vy * 2 + y) / 3.0
        points.append((x, y))

    draw(points)  # вызвали функцию

calculate(n=100000)  # ковер из такого кол-ва точек
