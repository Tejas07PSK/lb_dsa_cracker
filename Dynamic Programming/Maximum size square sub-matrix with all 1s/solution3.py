class Solution:
    def maxSquare (self, n, m, mat):
        glob_max = 0
        for i in range(len(mat) - 1, -1, -1):
            for j in range(len(mat[0]) - 1, -1, -1):
                if (mat[i][j] == 1):
                    left, left_down, down = 0, 0, 0
                    if ((j + 1) < len(mat[0])): left = mat[i][j + 1]
                    if (((j + 1) < len(mat[0])) and ((i + 1) < len(mat))): left_down = mat[i + 1][j + 1]
                    if ((i + 1) < len(mat)): down = mat[i + 1][j]
                    mat[i][j] = 1 + min(left, left_down, down)
                glob_max = max(glob_max, mat[i][j])
        return glob_max
