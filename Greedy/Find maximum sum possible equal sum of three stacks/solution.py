from typing import List
class Solution:
    def maxEqualSum(self, n1: int, n2: int, n3: int, s1: List[int], s2: List[int], s3: List[int]) -> int:
        tot1, tot2, tot3 = sum(s1), sum(s2), sum(s3)
        i, j, k = 0, 0, 0
        while ((i < n1) and (j < n2) and (k < n3)):
            if (tot1 == tot2 == tot3): return tot1
            mx_tot = max(tot1, tot2, tot3)
            if (mx_tot == tot1): tot1, i = tot1 - s1[i], i + 1
            elif (mx_tot == tot2): tot2, j = tot2 - s2[j], j + 1
            else: tot3, k = tot3 - s3[k], k + 1
        return 0
