from math import ceil
class Solution:
    def merge (self, arr1, arr2, n, m):
        gap = ceil((n + m) / 2)
        while (gap >= 1):
            i, j = 0, gap
            while ((i < (n + m)) and (j < (n + m))):
                if (i < n):
                    if (j < n):
                        if (arr1[i] > arr1[j]): arr1[i], arr1[j] = arr1[j], arr1[i]
                    else:
                        if (arr1[i] > arr2[j - n]): arr1[i], arr2[j - n] = arr2[j - n], arr1[i]
                else:
                    if (arr2[i - n] > arr2[j - n]): arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]
                i += 1
                j += 1
            if (gap == 1): break
            gap = ceil(gap / 2)
