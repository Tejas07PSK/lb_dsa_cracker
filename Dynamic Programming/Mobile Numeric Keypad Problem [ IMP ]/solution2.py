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
	    dp = [[None for j in range(10)] for i in range(N + 1)]
	    ans = 0
	    for n in range(1, N + 1):
	        for i in range(10):
	            if (n == 1): dp[n][i] = 1
	            else:
	                dp[n][i] = 0
	                for next_i in key_pad[i]: dp[n][i] += dp[n - 1][next_i]
	            if (n == N): ans += dp[n][i]
	    return ans
