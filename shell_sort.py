import time
from sort_result import SortResult


def shell_sort(arr, n=None) -> SortResult:
    start = time.time()
    comparisions = 0
    swaps = 0

    if n is None:
        n = len(arr) - 1
    # code here
    gap = n // 2

    while gap > 0:
        comparisions += 1
        j = gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j < n:
            comparisions += 1
            i = j - gap  # This will keep help in maintain gap value

            while i >= 0:
                comparisions += 1
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                comparisions += 1
                if arr[i + gap] > arr[i]:
                    break
                else:
                    swaps += 1
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]

                i = i - gap  # To check left side also
                # If the element present is greater than current element
            j += 1
        gap = gap // 2

    return SortResult(arr, comparisions, swaps, time.time() - start)
