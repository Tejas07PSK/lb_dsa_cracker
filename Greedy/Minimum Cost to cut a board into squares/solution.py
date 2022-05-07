from typing import List

class Solution:
    def minimumCostOfBreaking (self, x: List[int], y: List[int], col_size: int, row_size: int) -> int:
        i, j, cost = 0, 0, 0
        x.sort(reverse=True) ; y.sort(reverse=True)
        while ((i < col_size) and (j < row_size)):
            if (x[i] >= y[j]): i, cost = i + 1, cost + ((j + 1) * x[i])
            else: j, cost = j + 1, cost + ((i + 1) * y[j])
        while (i < col_size): i, cost = i + 1, cost + ((j + 1) * x[i])
        while (j < row_size): j, cost = j + 1, cost + ((i + 1) * y[j])
        return cost
