class Solution:
    def LCSof3 (self, A, B, C, n1, n2, n3):
        dp = [[[0 for k in range(n3 + 1)] for i in range(n1 + 1)] for j in range(n2 + 1)]
        for j in range(n2 - 1, -1, -1):
            for i in range(n1 - 1, -1, -1):
                for k in range(n3 - 1, -1, -1):
                    if ((A[i] == B[j]) and (B[j] == C[k])):
                        dp[j][i][k] = 1 + dp[j + 1][i + 1][k + 1]
                    else:
                        dp[j][i][k] = max(dp[j + 1][i][k], dp[j][i + 1][k], dp[j][i][k + 1])
        return dp[0][0][0]
