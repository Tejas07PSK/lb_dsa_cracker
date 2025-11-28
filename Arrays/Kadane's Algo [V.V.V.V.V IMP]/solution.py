class Solution:
    def maxSubArraySum (self, arr, n):
        curr_max, glob_max = arr[0], arr[0]
        for i in range(1, n):
            curr_max = max((curr_max + arr[i]), arr[i])
            glob_max = max(glob_max, curr_max)
        return glob_max

