import time
import numpy as np
from sort_result import SortResult
from typing import Tuple


def partition(arr, low, high) -> Tuple[int, int, int]:
    comparisions = 0
    swaps = 0

    pivot = arr[high]

    i = low - 1

    for j in range(low, high):
        comparisions += 1
        if arr[j] <= pivot:
            i = i + 1
            swaps += 1
            arr[i], arr[j] = arr[j], arr[i]

    swaps += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1, comparisions, swaps


def quickSort(arr: np.ndarray, low=0, high=None, comparisions=0, swaps=0) -> SortResult:
    start = time.time()
    if high is None:
        high = len(arr) - 1

    comparisions += 1
    if low < high:
        pi, p_comparisions, p_swaps = partition(arr, low, high)

        r1 = quickSort(arr, low, pi - 1, comparisions, swaps)
        r2 = quickSort(arr, pi + 1, high, comparisions, swaps)

        comparisions += p_comparisions + r1.comparisions + r2.comparisions
        swaps += p_swaps + r1.swaps + r2.swaps

    return SortResult(arr, comparisions, swaps, time.time() - start)
