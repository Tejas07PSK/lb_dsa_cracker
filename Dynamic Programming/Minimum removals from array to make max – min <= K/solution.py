from bisect import bisect
class Solution:
    def removals (self, arr, n, k):
        arr.sort()
        min_removals = n
        i = 0
        while (i < n):
            j = bisect(arr, (arr[i] + k), i + 1)
            min_removals = min(min_removals, i + (n - j))
            i += 1
        return min_removals
