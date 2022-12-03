class Solution:
    def __count_friends_helper(self, n):
        if (n == 0): return 0
        if (n == 1): return 1
        if (n == 2): return 2
        if (self.dp[n] == 0):
            self.dp[n] = (self.__count_friends_helper(n - 1)
            + ((n - 1) * self.__count_friends_helper(n - 2))) % self.mod
        return self.dp[n]

    def countFriendsPairings (self, n):
        self.dp = [0 for i in range(n + 1)]
        self.mod = 1000000007
        return self.__count_friends_helper(n)
