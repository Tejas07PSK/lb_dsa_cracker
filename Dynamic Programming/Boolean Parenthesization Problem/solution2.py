class Solution:
    def countWays (self, N, S):
        self.dp = [[[0, 0] for j in range(N)] for i in range(N)]
        for i in range(N - 1, -1, -2):
            self.dp[i][i] = [int(S[i] == 'T'), int(S[i] == 'F')]
            for j in range(i + 1, N):
                for k in range(i, j + 1):
                    if ((S[k] != 'T') and (S[k] != 'F')):
                        left_true_count, left_false_count = self.dp[i][k - 1]
                        right_true_count, right_false_count = self.dp[k + 1][j]
                        if (S[k] == '&'):
                            self.dp[i][j][0] += (left_true_count * right_true_count)
                            self.dp[i][j][1] += ((left_true_count * right_false_count) +
                                                 (left_false_count * right_true_count) +
                                                 (left_false_count * right_false_count))
                        elif (S[k] == '|'):
                            self.dp[i][j][0] += ((left_true_count * right_false_count) +
                                                 (left_false_count * right_true_count) +
                                                 (left_true_count * right_true_count))
                            self.dp[i][j][1] += (left_false_count * right_false_count)
                        elif (S[k] == '^'):
                            self.dp[i][j][0] += ((left_true_count * right_false_count) +
                                                 (left_false_count * right_true_count))
                            self.dp[i][j][1] += ((left_false_count * right_false_count) +
                                                 (left_true_count * right_true_count))
        return (self.dp[0][N - 1][0] % 1003)
