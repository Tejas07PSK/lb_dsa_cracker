class Solution:
	def getCount (self, N):
	    key_pad = [
	        [0, 8],
	        [1, 4, 2],
	        [2, 1, 3, 5],
	        [3, 2, 6],
	        [4, 1, 5, 7],
	        [5, 2, 4, 8, 6],
	        [6, 3, 5, 9],
	        [7, 4, 8],
	        [8, 5, 7, 0, 9],
	        [9, 6, 8]
	    ]
	    dp = [[None for j in range(10)] for i in range(2)]
	    ans = 0
	    for n in range(1, N + 1):
	        for i in range(10):
	            if (n == 1): dp[1][i] = 1
	            else:
	                dp[1][i] = 0
	                for next_i in key_pad[i]: dp[1][i] += dp[0][next_i]
	            if (n == N): ans += dp[1][i]
	        dp[0], dp[1] = dp[1], dp[0]
	    return ans
