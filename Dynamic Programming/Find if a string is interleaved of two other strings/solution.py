class Solution:
    def __is_inter_leave_helper (self, i, j, k, a, b, c):
        if ((i == len(a)) and (j == len(b)) and (k == len(c))): return True
        if (i == len(a)):
            if (j == len(b)): return False
            while (k < len(c)):
                if (b[j] != c[k]): return False
                j += 1 ; k += 1
            return True
        if (j == len(b)):
            if (i == len(a)): return False
            while (k < len(c)):
                if (a[i] != c[k]): return False
                i += 1 ; k += 1
            return True
        if (self.dp[i][j] == None):
            self.dp[i][j] = False
            if (a[i] == c[k]):
                if (self.__is_inter_leave_helper(i + 1, j, k + 1, a, b, c)):
                    self.dp[i][j] = True
            if ((not self.dp[i][j]) and (b[j] == c[k])):
                if (self.__is_inter_leave_helper(i, j + 1, k + 1, a, b, c)):
                    self.dp[i][j] = True
        return self.dp[i][j]

    def isInterleave (self, A, B, C):
        if (len(C) != (len(A) + len(B))): return False
        self.dp = [[None for j in range(len(B))] for i in range(len(A))]
        return self.__is_inter_leave_helper(0, 0, 0, A, B, C)
