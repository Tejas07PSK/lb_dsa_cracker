class Solution:
    def maximumPath (self, n, mat):
        glob_max = 0
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                down_right, down, down_left = 0, 0, 0
                if((i + 1) < n):
                    down = mat[i + 1][j]
                    if ((j + 1) < n): down_right = mat[i + 1][j + 1]
                    if ((j - 1) >= 0): down_left = mat[i + 1][j - 1]
                mat[i][j] = mat[i][j] + max(down, down_right, down_left)
                glob_max = max(glob_max, mat[i][j])
        return glob_max
