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
        pivot = arr[right] ; i, j = 0, right - 1
        while (True):
            while ((i <= right) and (arr[i] <= pivot)):
                i += 1
            while ((j >= left) and (arr[i] >= pivot)):
                j -= 1
            if (i >= j): break
            arr[i], arr[right] = arr[right], arr[i]
        return i
