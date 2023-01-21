class Solution:
    def smallestSumSubarray(self, arr, n):
        prev_max, prev_min, glob_min = arr[0], arr[0], arr[0]
        for i in range(1, n):
            curr_max = max((prev_max + arr[i]), (prev_min + arr[i]), arr[i])
            curr_min = min((prev_max + arr[i]), (prev_min + arr[i]), arr[i])
            glob_min = min(glob_min, curr_min)
            prev_max = curr_max
            prev_min = curr_min
        return glob_min
