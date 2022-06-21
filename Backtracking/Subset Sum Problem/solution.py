class Solution:
    def equalPartition (self, n, arr):
        tot = sum(arr)
        if ((tot % 2) != 0): return False
        tot, dp = (tot // 2), {0}
        for num in arr:
            new_dp = set()
            for ele in dp:
                curr_sum = num + ele
                if (curr_sum not in dp): 
                    if (curr_sum == tot): return True
                    new_dp.add(curr_sum)
                new_dp.add(ele)
            del dp
            dp = new_dp
        return False
