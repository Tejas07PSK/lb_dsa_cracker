class Solution:
    def __pre_process (self, mat):
        mat[0][0] = 0
        n1, n2 = len(mat), len(mat[0])
        for i in range(1, n2):
            mat[0][i] = mat[0][i - 1] + 1
        for i in range(1, n1):
            mat[i][0] = mat[i - 1][0] + 1

    def editDistance (self, s, t):
        n1, n2 = len(s) + 1, len(t) + 1
        mat = [[0 for j in range(n2)] for i in range(n1)]
        self.__pre_process(mat)
        for i in range(1, n1):
            for j in range(1, n2):
                mat[i][j] = (min(mat[i][j - 1], mat[i - 1][j - 1], mat[i - 1][j]) + 1) if s[i - 1] != t[j - 1] else mat[i - 1][j - 1]
        return mat[n1 - 1][n2 - 1]
