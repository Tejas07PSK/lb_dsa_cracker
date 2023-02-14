class Solution:
    def __get_count_helper (self, i, N):
        if (N == 1): return 1
        if (self.dp[N][i] == None):
            self.dp[N][i] = 0
            for next_i in self.key_pad[i]:
                self.dp[N][i] += self.__get_count_helper(next_i, N - 1)
        return self.dp[N][i]
        
	def getCount (self, N):
	    self.key_pad = [
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
	    self.dp = [[None for j in range(10)] for i in range(N + 1)]
	    ans = 0
	    for i in range(10): ans += self.__get_count_helper(i, N)
	    return ans
