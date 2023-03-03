class Solution:
    def merge (self, arr1, arr2, n, m):
        i, j = n - 1, 0
        while ((i >= 0) and (j < m) and (arr1[i] > arr2[j])):
            arr1[i], arr2[j] = arr2[j], arr1[i]
            i -= 1
            j += 1
        arr1.sort()
        arr2.sort()
