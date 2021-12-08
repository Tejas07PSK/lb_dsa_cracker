class Solution:
    def __init_mat (self, r, c):
        return [[0 for i in range(r)] for j in range(c)]

    def __swap (self, list, idx1, idx2):
        temp = list[idx1]
        list[idx1] = list[idx2]
        list[idx2] = temp

    def LongestRepeatingSubsequence(self, s):
        n = len(s)
        mat = self.__init_mat((n + 1), 2)
        for i in range(1, (n + 1)):
            for j in range(1, (n + 1)):
                if ((s[i - 1] == s[j - 1]) and (i != j)):
                    mat[1][j] = 1 + mat[0][j - 1]
                else:
                    mat[1][j] = max(mat[0][j], mat[1][j - 1])
            self.__swap(mat, 0, 1)
        return mat[0][n]
