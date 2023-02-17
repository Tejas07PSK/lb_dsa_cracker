from math import inf
class Solution:
    def maximumSumRectangle (self, R, C, M):
        glb_mx_rct_sum = -inf
        tmp_row_sum_arr = [0 for i in range(R)]
        for col_left in range(C):
            for col_right in range(col_left, C):
                for row in range(R): tmp_row_sum_arr[row] += M[row][col_right]
                mx_rct_sum, curr_rct_sum = tmp_row_sum_arr[0], tmp_row_sum_arr[0]
                if (col_right == (C - 1)): tmp_row_sum_arr[0] = 0
                for row in range(1, R):
                    curr_rct_sum = max((curr_rct_sum + tmp_row_sum_arr[row]), tmp_row_sum_arr[row])
                    mx_rct_sum = max(mx_rct_sum, curr_rct_sum)
                    if (col_right == (C - 1)): tmp_row_sum_arr[row] = 0
                glb_mx_rct_sum = max(glb_mx_rct_sum, mx_rct_sum)
        return glb_mx_rct_sum
