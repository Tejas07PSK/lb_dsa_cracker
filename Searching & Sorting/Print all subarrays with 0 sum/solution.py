class Solution:
    def findSubArrays (self, arr, n):
        map = {}
        i, sum_so_far = 0, 0
        res = 0
        while (i < n):
            sum_so_far += arr[i]
            if (sum_so_far == 0):
                res += 1
            if sum_so_far in map:
                res += map[sum_so_far]
                map[sum_so_far] += 1
            else:
                map[sum_so_far] = 1
            i += 1
        return res
