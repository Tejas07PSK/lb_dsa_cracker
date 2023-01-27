class Solution:
    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s //= 2
        dp = {0}
        for element in arr:
            tmp_dp = set()
            for sum_before in dp:
                if ((sum_before + element) == s): return 1
                tmp_dp.add(sum_before)
                tmp_dp.add(sum_before + element)
            del dp
            dp = tmp_dp
        return 0
