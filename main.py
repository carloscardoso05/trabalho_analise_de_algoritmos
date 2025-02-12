from dataclasses import dataclass
from typing import Callable, Any, List

import matplotlib.pyplot as plt
import numpy as np
from heap_sort import heap_sort
from quick_sort import quick_sort
from shell_sort import shell_sort
from sort_result import SortResult


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


@dataclass
class TestResult:
    times: List[float]
    swaps: List[int]
    comparisons: List[int]
    sizes: List[int]


def test_sort(sort_function: Callable[[np.ndarray], SortResult], array: np.ndarray, *, intervals: int,
              repeat: int) -> TestResult:
    array = array.copy()
    step = len(array) // intervals
    times = []
    swaps = []
    comparisons = []
    sizes = []
    for size in range(0, len(array) + step, step):
        print(f"\r{size} - {size / (len(array)) * 100:.2f}%", end="")
        sizes.append(size)
        total_time = 0.0
        total_swap = 0
        total_comparison = 0
        for _ in range(repeat):
            result = sort_function(array)
            total_time += result.elapsed_time
            total_swap += result.swaps
            total_comparison += result.comparisions
        times.append(total_time)
        swaps.append(total_swap)
        comparisons.append(total_comparison)
    return TestResult(times, swaps, comparisons, sizes)


def main():
    import sys
    sys.setrecursionlimit(2 ** 16)
    array = random_array(10000)
    results = []
    for sort in [(shell_sort, 'Shell Sort'), (heap_sort, 'Heap Sort'), (quick_sort, 'Quick Sort')]:
        result = test_sort(
            sort[0],
            array,
            intervals=10,
            repeat=10
        )
        results.append((result, sort[1]))
        plt.plot(result.sizes, result.times, label=sort[1], marker='o')
    plt.title("Vetor aleatório")
    plt.xlabel("Tamanho do vetor")
    plt.ylabel("Tempo (s)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
