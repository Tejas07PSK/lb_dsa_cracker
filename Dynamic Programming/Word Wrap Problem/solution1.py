from math import inf
class Solution:
    def __solve_word_wrap (self, i, nums, k):
        if (i == len(nums)): return 0
        if (self.dp[i] == None):
            self.dp[i], tot, spc_in_bet = inf, 0, -1
            for j in range(i, len(nums)):
                tot += nums[j] ; spc_in_bet += 1
                if ((tot + spc_in_bet) > k): break
                tmp = ((k - (tot + spc_in_bet)) ** 2) if ((j + 1) != len(nums)) else 0
                self.dp[i] = min(self.dp[i], tmp + self.__solve_word_wrap(j + 1, nums, k))
        return self.dp[i]

	def solveWordWrap (self, nums, k):
	    self.dp = [None for i in range(len(nums) + 1)]
	    return self.__solve_word_wrap(0, nums, k)
