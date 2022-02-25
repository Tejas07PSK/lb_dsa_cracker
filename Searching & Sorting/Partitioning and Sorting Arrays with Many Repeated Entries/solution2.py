import random

class Solution:
    def quickSort (self, left, right, arr):
        size = right - left + 1
        if (size < 2): return
        if (size == 2):
            if (arr[left] > arr[right]):
                arr[left], arr[right] = arr[right], arr[left]
            return
        mid1, mid2 = self.partitionIndex(left, right, arr)
        self.quickSort(left, mid1, arr) ; self.quickSort(mid2, right, arr)

    def partitionIndex (self, left, right, arr):
        idx = random.randint(left, right) ; arr[idx], arr[right] = arr[right], arr[idx]
        pivot = arr[right] ; i, j, k = 0, 0, right
        while (i <= k):
            if (arr[i] < pivot):
                arr[j], arr[i] = arr[i], arr[j] ; i += 1 ; j += 1
            elif (arr[i] == pivot): i += 1
            else:
                arr[i], arr[k] = arr[k], arr[i] ; k -= 1
        return j - 1, k + 1
