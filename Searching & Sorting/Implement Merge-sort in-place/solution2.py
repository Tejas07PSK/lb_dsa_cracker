from math import ceil
class Solution:
    def merge (self, l, r, arr):
        gap = ceil((r - l + 1) / 2)
        while (gap >= 1):
            i, j = l, l + gap
            while ((i <= r) and (j <= r)):
                if (arr[i] > arr[j]): arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j += 1
            if (gap == 1): break
            gap = ceil(gap / 2)

    def mergeSortInPlace (self, l, r, arr):
        sz = r - l + 1
        if (sz < 2): return
        elif (sz == 2):
            if (arr[l] > arr[r]): arr[l], arr[r] = arr[r], arr[l]
        else:
            mid = l + ((r - l) // 2)
            self.mergeSortInPlace(l, mid, arr)
            self.mergeSortInPlace(mid + 1, r, arr)
            self.merge(l, r, arr)

arr = [7, 7, 3, 1, 2, -3, 3, -4, 13, 9, 8, 9, 10, 1]
Solution().mergeSortInPlace(0, len(arr) - 1, arr)
print(arr)
