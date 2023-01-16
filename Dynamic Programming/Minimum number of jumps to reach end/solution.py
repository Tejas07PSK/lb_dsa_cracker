from math import inf
class Solution:
    def minJumps (self, arr, n):
        i, jumps = 0, 0
        while (i < (n - 1)):
            if (arr[i] == 0):
                jumps = -1
                break
            jumps += 1
            if ((i + arr[i]) >= (n - 1)): break
            j = i + 1
            rng_end = i + arr[i]
            i, min_diff = inf, inf
            while (j <= rng_end):
                curr_diff = n - 1 - j - arr[j]
                if (curr_diff <= min_diff):
                    min_diff = curr_diff
                    i = j
                j += 1
        return jumps
