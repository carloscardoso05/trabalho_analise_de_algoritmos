import matplotlib.pyplot as plt
import numpy as np
from heap_sort import heapSort
from quick_sort import quickSort
from shell_sort import shellSort


def random_array(t) -> np.ndarray:
    t = int(t)
    import random

    return np.array([random.randint(0, t) for _ in range(t)])


def reversed_array(t) -> np.ndarray:
    t = int(t)
    return np.array(list(range(t, 0, -1)))


def sorted_array(t) -> np.ndarray:
    t = int(t)
    return np.array(list(range(t)))


if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(2 ** 16)
    for sort in [shellSort, heapSort, quickSort]:
        times = []
        sizes = []
        max_size = 1000
        steps = max_size // 10
        repeat = 10
        for size in range(0, max_size + steps, steps):
            print(f"\r{size} - {size / (max_size + steps) * 100:.2f}%", end="")
            sizes.append(size)
            arr = reversed_array(size)
            total_time = 0.0
            for _ in range(repeat):
                arr_copy = arr.copy()
                result = sort(arr_copy)
                partial_time = result.swaps
                total_time += partial_time
            times.append(total_time)
        plt.plot(sizes, times, label=str(sort))
    plt.show()
