import math

class Solution:
    def merge (self, arr1, arr2, n, m):
        gap = math.ceil((n + m) / 2)
        while (gap >= 1):
            i = 0
            j = i + gap
            while ((i < (n + m)) and (j < (n + m))):
                if (i < n):
                    if (j < n):
                        if (arr1[i] > arr1[j]):
                            temp = arr1[i]
                            arr1[i] = arr1[j]
                            arr1[j] = temp
                    else:
                        if (arr1[i] > arr2[j - n]):
                            temp = arr1[i]
                            arr1[i] = arr2[j - n]
                            arr2[j - n] = temp
                else:
                    if (arr2[i - n] > arr2[j - n]):
                        temp = arr2[i - n]
                        arr2[i - n] = arr2[j - n]
                        arr2[j - n] = temp
                i += 1
                j = i + gap
            if (gap == 1):
                break
            gap = math.ceil(gap / 2)
