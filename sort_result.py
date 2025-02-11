from dataclasses import dataclass

import numpy as np


@dataclass
class SortResult:
    arr: np.ndarray
    comparisions: int
    swaps: int
    elapsed_time: float
