class Solution:
    def equalPartition (self, n, arr):
        s = sum(arr)
        if ((s % 2) != 0): return 0
        s = s // 2
        dp = {0}
        for num in arr:
            new_dp = set()
            for tot in dp:
                if ((tot + num) == s): return 1
                new_dp.add(tot)
                new_dp.add(tot + num)
            del dp
            dp = new_dp
        return 0
