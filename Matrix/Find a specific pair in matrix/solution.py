import math

class Solution:
    def pre_process (self, matrix, r, c):
        i, j = (r - 2), (c - 1)
        temp_matrix = [[0] * len(matrix)] * len(matrix[0])
        temp_matrix[-1][-1] = matrix[-1][-1]
        while (i >= 0):
            temp_matrix[i][j] = max(matrix[i][j], temp_matrix[i + 1][j])
            i -= 1
        i = (r - 1) ; j -= 1
        while (j >= 0):
            temp_matrix[i][j] = max(matrix[i][j], temp_matrix[i][j + 1])
            j -= 1
        return temp_matrix

    def findSpecificPairWithMaxDiff (self, matrix):
        r, c = len(matrix), len(matrix[0])
        temp_matrix = self.pre_process(matrix, r, c)
        max_res = -math.inf
        i = (r - 2)
        while (i >= 0):
            j = (c - 2)
            while (j >= 0):
                max_res = max(max_res, (temp_matrix[i + 1][j + 1] - matrix[i][j]))
                temp_matrix[i][j] = max(matrix[i][j], temp_matrix[i + 1][j], temp_matrix[i][j + 1])
                j -= 1
            i -= 1
        return max_res
