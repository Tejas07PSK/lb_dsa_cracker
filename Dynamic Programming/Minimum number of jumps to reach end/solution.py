from math import inf
class Solution:
    def minJumps (self, arr, n):
        i, jumps = 0, 0
        while (i < (n - 1)):
            j = i + 1
            rng_end = i + arr[i]
            i, min_diff = inf, inf
            while (j <= rng_end ):
                end_pos = j + arr[j]
                if (end_pos >= (n - 1)):
                    i = end_pos ; break
                if (arr[end_pos] != 0):
                    curr_diff = n - 1 - end_pos
                    if (curr_diff <= min_diff):
                        min_diff = curr_diff
                        i = end_pos
                j += 1
            if (i != inf): jumps += 1
            else: jumps = -1
        return jumps
