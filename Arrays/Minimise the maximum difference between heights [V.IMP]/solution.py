class Solution:
    def getMinDiff (self, arr, n, k):
        arr.sort()
        diff = arr[-1] - arr[0]
        mn, mx = None, None
        for i in range(n - 1):
            mn = min(arr[0] + k, arr[i + 1] - k)
            mx = max(arr[-1] - k, arr[i] + k)
            if (mn >= 0): diff = min(diff, (mx - mn))
        return diff
