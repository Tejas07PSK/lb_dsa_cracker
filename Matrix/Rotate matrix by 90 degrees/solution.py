class Solution:
    def swap_idx_val_mat (self, matrix, i1, j1, i2, j2):
        temp = matrix[i1][j1]
        matrix[i1][j1] = matrix[i2][j2]
        matrix[i2][j2] = temp

    def rotate (self, matrix: List[List[int]]) -> None:
        N = len(matrix)
        layers = (N + 1) // 2
        l = 0
        while (l < layers):
            row_start, row_end = (0 + l), (N - l - 1)
            if (row_start == row_end):
                break
            col_start, col_end = (0 + l), (N - l - 1)
            upper_side_i, upper_side_j = row_start, col_start
            i, j = row_start, col_end
            while (i < row_end):
                self.swap_idx_val_mat(matrix, upper_side_i, upper_side_j, i, j)
                upper_side_j += 1 ; i += 1
            upper_side_j = col_start
            while (j > col_start):
                self.swap_idx_val_mat(matrix, upper_side_i, upper_side_j, i, j)
                upper_side_j += 1 ; j -= 1
            upper_side_j = col_start
            while (i > row_start):
                self.swap_idx_val_mat(matrix, upper_side_i, upper_side_j, i, j)
                upper_side_j += 1 ; i -= 1
            l += 1
