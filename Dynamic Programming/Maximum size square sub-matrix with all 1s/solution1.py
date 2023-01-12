class Solution:    
    def __max_square_helper (self, i, j, mat):
        if ((i == len(mat)) or (j == len(mat[0]))): return 0
        if (self.dp[i][j] == None):
            left = self.__max_square_helper(i, j + 1, mat)
            left_down = self.__max_square_helper(i + 1, j + 1, mat)
            down = self.__max_square_helper(i + 1, j, mat)
            self.dp[i][j] = 0
            if (mat[i][j] == 1): self.dp[i][j] = 1 + min(left, left_down, down)
            self.glob_max = max(self.glob_max, self.dp[i][j])
        return self.dp[i][j]

    def maxSquare (self, n, m, mat):
        self.dp = [[None for j in range(len(mat[0]))] for i in range(len(mat))]
        self.glob_max = 0 ; self.__max_square_helper(0, 0, mat)
        return self.glob_max
