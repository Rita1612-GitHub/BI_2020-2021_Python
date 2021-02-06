from random import shuffle, uniform
from statistics import mean
from time import time
from matplotlib import pyplot as plt


def _get_range():
    return range(2, 9)


def is_sorted(arr):
    flag = False
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            flag = True
    return not flag


sample_array = [1,5,8,90]
print(f'Is {sample_array} array sorted?: {is_sorted(sample_array)}')


def bogosort(arr):
    start = time()
    while not is_sorted(arr):
        shuffle(arr)
    end = time()
    return end - start


# plt.plot(list(_get_range()), [mean([bogosort([int(uniform(0, 100000)) for _ in range(y)]) for _ in range(3)]) for y in _get_range()])


result = []
for y in _get_range():
    timings = []
    for _ in range(3):
        array = []
        for _ in range(y):
            array.append(int(uniform(0, 100000)))
        time_sec = bogosort(array)
        timings.append(time_sec)
    mean_time = mean(timings)
    result.append(mean_time)

plt.plot(list(_get_range()), result)
plt.title("Monkey sort running time", fontsize=10)
plt.xlabel("Array size")
plt.ylabel("Running time, s")
plt.show()
