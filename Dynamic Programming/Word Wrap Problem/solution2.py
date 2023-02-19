from math import inf
class Solution:
	def solveWordWrap (self, nums, k):
	    dp = [inf for i in range(len(nums) + 1)] ; dp[-1] = 0
	    for i in range(len(nums) - 1, -1, -1):
	        tot, spc_in_bet = 0, -1
	        for j in range(i, len(nums)):
	            tot += nums[j] ; spc_in_bet += 1
	            if ((tot + spc_in_bet) > k): break
	            tmp = ((k - (tot + spc_in_bet)) ** 2) if ((j + 1) != len(nums)) else 0
	            dp[i] = min(dp[i], tmp + dp[j + 1])
	    return dp[0]
