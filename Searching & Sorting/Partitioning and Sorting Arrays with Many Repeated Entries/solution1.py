import random

class Solution:
    def quickSort (self, left, right, arr):
        size = right - left + 1
        if (size < 2): return
        if (size == 2):
            if (arr[left] > arr[right]):
                arr[left], arr[right] = arr[right], arr[left]
            return
        mid = self.partitionIndex(left, right, arr)
        self.quickSort(left, (mid - 1), arr) ; self.quickSort((mid + 1), right, arr)

    def partitionIndex (self, left, right, arr):
        idx = random.randint(left, right) ; arr[idx], arr[right] = arr[right], arr[idx]
        pivot = arr[right] ; i, j = 0, 0
        while (i <= right):
            if (arr[i] <= pivot):
                arr[j], arr[i] = arr[i], arr[j] ; i += 1 ; j += 1
            else: i += 1
        return j - 1
