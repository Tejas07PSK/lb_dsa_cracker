class Solution:
    def maxSumPairWithDifferenceLessThanK (self, arr, n, k):
        arr.sort() ; n = len(arr)
        tot = 0
        i = -1
        while (i > -n):
            if ((arr[i] - arr[i - 1]) < k):
                tot += (arr[i] + arr[i - 1])
                i -= 2
            else: i -= 1
        return tot
