from typing import List
class Solution:
    def sumZeroMatrix (self, a: List[List[int]]) -> List[List[int]]:
        row_sz, col_sz = len(a), len(a[0])
        mx_rct_ar = -1
        mx_rct_row_start, mx_rct_row_end = -1, -1
        mx_rct_col_start, mx_rct_col_end = -1, -1
        tmp_row_sum_arr = [0 for i in range(row_sz)]
        seen_before = {}
        for col_left in range(col_sz):
            for col_right in range(col_left, col_sz):
                for row in range(row_sz): tmp_row_sum_arr[row] += a[row][col_right]
                mx_col_sz = col_right - col_left + 1
                mx_row_sz, mx_row_start, mx_row_end = -1, -1, -1
                tot = 0
                for row in range(row_sz):
                    tot += tmp_row_sum_arr[row]
                    if (tmp_row_sum_arr[row] == 0):
                        if (1 > mx_row_sz):
                            mx_row_start, mx_row_end, mx_row_sz = row, row, 1
                    if (tot == 0):
                        if ((row + 1) > mx_row_sz):
                            mx_row_start, mx_row_end, mx_row_sz = 0, row, row + 1
                    if (tot in seen_before):
                        if ((row - seen_before[tot]) > mx_row_sz):
                            mx_row_start, mx_row_end, mx_row_sz = seen_before[tot] + 1, row, (row - seen_before[tot])
                    else: seen_before[tot] = row
                    if (col_right == (col_sz - 1)): tmp_row_sum_arr[row] = 0
                if ((mx_row_sz * mx_col_sz) > (mx_rct_ar)):
                    mx_rct_ar = (mx_row_sz * mx_col_sz)
                    mx_rct_row_start = mx_row_start
                    mx_rct_row_end = mx_row_end
                    mx_rct_col_start = col_left
                    mx_rct_col_end = col_right
                seen_before.clear()
        if (mx_rct_ar == -1): return []
        return [[a[i][j] for j in range(mx_rct_col_start, mx_rct_col_end + 1)] for i in range(mx_rct_row_start, mx_rct_row_end + 1)]
