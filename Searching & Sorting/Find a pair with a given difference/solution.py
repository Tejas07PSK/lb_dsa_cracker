from bisect import bisect_left

class Solution:
    def findPair (self, arr, l, n):
        arr.sort()
        for i in range(l - 1):
            key = arr[i] + n
            j = bisect_left(arr, key, (i + 1))
            if ((j != l) and (arr[j] == key)):
                return True
        return False
