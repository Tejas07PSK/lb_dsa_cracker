def maximumArea (mat, n, m):
    row_sz, col_sz = len(mat), len(mat[0])
    mx_rct_ar = 0
    tmp_row_sum_arr = [0 for i in range(row_sz)]
    seen_before = {}
    for col_left in range(col_sz):
        for col_right in range(col_left, col_sz):
            for row in range(row_sz): tmp_row_sum_arr[row] += mat[row][col_right] if (mat[row][col_right] == 1) else -1
            mx_col_sz = col_right - col_left + 1
            mx_row_sz = 0
            tot = 0
            for row in range(row_sz):
                tot += tmp_row_sum_arr[row]
                if (tmp_row_sum_arr[row] == 0): mx_row_sz = max(mx_row_sz, 1)
                if (tot == 0): mx_row_sz = max(mx_row_sz, (row + 1))
                if (tot in seen_before): mx_row_sz = max(mx_row_sz, (row - seen_before[tot])) 
                else: seen_before[tot] = row
                if (col_right == (col_sz - 1)): tmp_row_sum_arr[row] = 0
            mx_rct_ar = max(mx_rct_ar, (mx_row_sz * mx_col_sz))
            seen_before.clear()
    return mx_rct_ar
