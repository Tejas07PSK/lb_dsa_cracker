class Solution:
    def __count_ways_helper (self, i, j, string):
        if (i == j):
            self.dp[i][j] = [int(string[i] == 'T'), int(string[i] == 'F')]
            return self.dp[i][j]
        if (self.dp[i][j] == None):
            self.dp[i][j] = [0, 0]
            for k in range(i, j + 1):
                if ((string[k] != 'T') and (string[k] != 'F')):
                    left_true_count, left_false_count = self.__count_ways_helper(i, k - 1, string)
                    right_true_count, right_false_count = self.__count_ways_helper(k + 1, j, string)
                    if (string[k] == '&'):
                        self.dp[i][j][0] += (left_true_count * right_true_count)
                        self.dp[i][j][1] += ((left_true_count * right_false_count) +
                                             (left_false_count * right_true_count) +
                                             (left_false_count * right_false_count))
                    elif (string[k] == '|'):
                        self.dp[i][j][0] += ((left_true_count * right_false_count) +
                                             (left_false_count * right_true_count) +
                                             (left_true_count * right_true_count))
                        self.dp[i][j][1] += (left_false_count * right_false_count)
                    elif (string[k] == '^'):
                        self.dp[i][j][0] += ((left_true_count * right_false_count) +
                                             (left_false_count * right_true_count))
                        self.dp[i][j][1] += ((left_false_count * right_false_count) +
                                             (left_true_count * right_true_count))
        return self.dp[i][j]

    def countWays (self, N, S):
        self.dp = [[None for j in range(N)] for i in range(N)]
        return (self.__count_ways_helper(0, N - 1, S)[0] % 1003)
