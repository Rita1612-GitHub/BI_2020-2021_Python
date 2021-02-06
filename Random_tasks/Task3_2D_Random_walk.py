import numpy as np
from matplotlib import pyplot as plt

dim = 2  # размерность
n = 10000  # кол-во точек
point_set = [-1, 0, 1]  # куда можно двигаться
start_point = np.zeros((1, dim))  # стартовая точка

arr = (n, dim)  # двумерный массив с нужным кол-вом точек
steps = np.random.choice(a=point_set, size=arr)  # заполнили массив случайными точками
path = np.concatenate([start_point, steps]).cumsum(
    0)  # сначала добавили к массиву начальную точку, а потом просуммировали
start = path[:1]  # первая строчка в массиве
stop = path[-1:]  # последняя строчка в массиве

figure = plt.figure(figsize=(8, 8), dpi=200)  # размер изображения
axes = figure.add_subplot()  # добавляет оси на рисунок
axes.scatter(path[:, 0], path[:, 1], c='blue', alpha=0.25, s=0.05)  # визуализация точек на пути синим цветом
axes.plot(path[:, 0], path[:, 1], c='blue', alpha=0.5, lw=0.25, ls='--')  # добавили пунктирную линию
axes.plot(start[:, 0], start[:, 1], c='red', marker='+')  # start point красная
axes.plot(stop[:, 0], stop[:, 1], c='green', marker='+')  # stop point зеленая
plt.title('2D Random Walk', size=12)  # название рисунка
plt.xlabel("x")  # подпись оси x
plt.ylabel("y")  # подпись оси y
plt.tight_layout(pad=5)  # подгоняет оси под размер рисунка, есть отступ от края рисунка
plt.show()
# plt.savefig('plots/random_walk_2d.png',dpi=250)
