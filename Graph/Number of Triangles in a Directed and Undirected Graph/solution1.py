from typing import List

class Solution:
    def numberOfTriangles (self, n: int, g: List[List[int]]) -> int:
        if (n < 3): return 0
        res = 0
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if ((i != j) and (i != k) and (j != k) and (g[i][j] == 1) and (g[j][k] == 1) and (g[k][i] == 1)):
                        res += 1
        return (res // 3)
