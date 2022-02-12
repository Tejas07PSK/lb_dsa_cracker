import io, os, sys

def size_of_bcs ():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, m = map(int, input().decode().split(' ')) ; k1 = [list(map(int, input().decode().split(' '))) for i in range(n)]
    x, y = map(int, input().decode().split(' ')) ; k2 = [list(map(int, input().decode().split(' '))) for j in range(x)]
    min_size = min(n, m, x, y) ; pwr_arr = [1 for i in range(min_size)] ; for i in range(1, min_size): pwr_arr[i] = pwr_arr[i - 1] * 1000
    roll_hash = [0 for i in range(min_size)]; found_k1, found_k2 = set(), set()
    low, high, ans = 0, min_size, 0
    while (low <= high):
        mid = low + ((high - low) // 2)

        col, prev_col_sum, p_ptr = mid - 1, 0, 0
        while (col >= 0):
            row = mid - 1
            while (row >= 0):
                roll_hash[0] += 
            col -= 1
        p_ptr, i = 0, mid - 1
        while (i >= 0):
            j = mid - 1
            while (j >= 0):
                roll_hash[0] += k1[i][j] * pwr_arr[p_ptr] ; p_ptr += 1 ; j -= 1
            i -= 1
        found_k1.add(roll_hash[0]) ; k = 1
        k1_col_start, k1_col_end = 1, mid
        while (k1_col_end < m):
            row, l_side_sum, r_side_sum, l_pwr_ptr, r_pwr_ptr = mid - 1, 0, 0, mid - 1, 0
            while (row >= 0):
                l_side_sum += k1[row][k1_col_start] * pwr_arr[l_pwr_ptr] ; r_side_sum += k1[row][k1_col_end] * pwr_arr[r_pwr_ptr]
                l_pwr_ptr += mid ; r_pwr_ptr += mid ; row += 1
            roll_hash[k] = roll_hash[k - 1] - l_side
            k1_col_start += 1 ; k1_col_end += 1
        k1_row_start, k1_row_end = 0, mid - 1
        cm_sq_fnd = False
        while (k1_row_end < n):
            k1_col_start, k1_col_end = 0, mid - 1
            while (k1_col_end < m):
                k2_row_start, k2_row_end = 0, mid - 1
                while (k2_row_end < x):
                    k2_col_start, k2_col_end = 0, mid - 1
                    while (k2_col_end < y):
                        i, k, flag = k1_row_start, k2_row_start, True
                        while (i <= k1_row_end):
                            j, l = k1_col_start, k2_col_start
                            while (j <= k1_col_end):
                                if (k1[i][j] != k2[k][l]):
                                    flag = False ; break
                                j += 1 ; l += 1
                            if (not flag):
                                break
                            i += 1 ; k += 1
                        if (flag):
                            cm_sq_fnd = True ; break
                        k2_col_start += 1 ; k2_col_end += 1
                    if (cm_sq_fnd):
                        break
                    k2_row_start += 1 ; k2_row_end += 1
                if (cm_sq_fnd):
                    break
                k1_col_start += 1 ; k1_col_end += 1
            if (cm_sq_fnd):
                break
            k1_row_start += 1 ; k1_row_end += 1
        if (cm_sq_fnd):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    sys.stdout.write(str(ans) + '\n')

size_of_bcs()