class Solution:
    def shortest_distance (self, matrix):
        n = len(matrix)
        for k in range(n):
            for i in range(n):
                if (i == k): continue
                for j in range(n):
                    if ((j == i) or (j == k)): continue
                    dist = -1 if (matrix[i][k] == -1) else matrix[i][k]
                    if (dist != -1): dist = -1 if (matrix[k][j] == -1) else (dist + matrix[k][j])
                    if (matrix[i][j] == -1): matrix[i][j] = -1 if (dist == -1) else dist
                    elif (dist != -1): matrix[i][j] = min(matrix[i][j], dist)
        return matrix
