from time import time
import random
import matplotlib.pyplot as plt
import numpy

def _get_range():
    return range(1000000, 10000000, 1000000)

def track_time(f):
    results = []
    for i in _get_range():
        results.append(f(i))
    return results

def calc_random(times):
    """
    Calculates execution time in seconds
    :param times: count for calling random()
    :return: execution time in seconds
    """
    start = time()
    [random.random() for i in range(times)]
    end = time()
    return end - start


def calc_numpy(times):
    start = time()
    numpy.random.random(size=times)
    end = time()
    return end - start


random_res = track_time(calc_random)
numpy_res = track_time(calc_numpy)
print(random_res)
print(numpy_res)

plt.plot(list(_get_range()), random_res)
plt.plot(list(_get_range()), numpy_res)
plt.title('Random vs numpy', fontsize=20)
plt.xlabel("Количество чисел")
plt.ylabel("Время выполнения программы, сек")
plt.show()
