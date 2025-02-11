from typing import Tuple
import time
import numpy as np

from sort_result import SortResult


def heapify(arr: np.ndarray, n: int, i: int) -> Tuple[int, int]:
    comparisions = 0
    swaps = 0
    while True:
        largest = i  # Initialize largest as root
        left = 2 * i + 1  # left = 2*i + 1
        right = 2 * i + 2  # right = 2*i + 2

        # If left child exists and is greater than root
        comparisions += 2
        if left < n and arr[left] > arr[largest]:
            largest = left

        # If right child exists and is greater than the largest so far
        comparisions += 2
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If largest is still root, then the subtree is a heap
        if largest == i:
            break

        # Otherwise, swap and continue heapifying the affected subtree
        swaps += 1
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
    return comparisions, swaps


def heapSort(arr: np.ndarray) -> SortResult:
    start = time.time()
    comparisions = 0
    swaps = 0
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        h_comparisions, h_swaps = heapify(arr, n, i)
        comparisions += h_comparisions
        swaps += h_swaps

    for i in range(n - 1, 0, -1):
        swaps += 1
        arr[0], arr[i] = arr[i], arr[0]

        h_comparisions, h_swaps = heapify(arr, i, 0)
        comparisions += h_comparisions
        swaps += h_swaps

    return SortResult(arr, comparisions, swaps, time.time() - start)
