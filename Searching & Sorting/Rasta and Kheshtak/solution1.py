import io, os, sys

def size_of_bcs ():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, m = map(int, input().decode().split(' ')) ; k1 = [list(map(int, input().decode().split(' '))) for i in range(n)]
    x, y = map(int, input().decode().split(' ')) ; k2 = [list(map(int, input().decode().split(' '))) for j in range(x)]
    min_size = min(n, m, x, y) ; pwr_arr = [1 for i in range((min_size * min_size) + 1)]
    for i in range(1, ((min_size * min_size) + 1)): pwr_arr[i] = pwr_arr[i - 1] * 1000
    roll_hash = [0 for i in range(max(m, y))]; found_k1 = set()
    low, high, ans = 1, min_size, 0
    while (low <= high):
        mid = low + ((high - low) // 2)
        p_ptr, i = 0, mid - 1
        roll_hash[0] = 0
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
                l_side_sum += k1[row][k1_col_start - 1] * pwr_arr[l_pwr_ptr] ; r_side_sum += k1[row][k1_col_end] * pwr_arr[r_pwr_ptr]
                l_pwr_ptr += mid ; r_pwr_ptr += mid ; row -= 1
            roll_hash[k] = ((roll_hash[k - 1] - l_side_sum) * 1000) + r_side_sum ; found_k1.add(roll_hash[k]) ; k += 1
            k1_col_start += 1 ; k1_col_end += 1
        k1_row_start, k1_row_end = 1, mid
        while (k1_row_end < n):
            k1_col_start, k1_col_end = 0, mid - 1
            up_row_sum, down_row_sum, roll_hash_ptr = 0, 0, 0
            while (k1_col_end < m):
                if (k1_col_start == 0):
                    k = 1
                    for i in range(k1_col_start, k1_col_end + 1):
                        up_row_sum += k1[k1_row_start - 1][i] * pwr_arr[(mid - k) + ((mid - 1) * mid)]
                        down_row_sum += k1[k1_row_end][i] * pwr_arr[(mid - k)] ; k += 1
                else:
                    up_row_sum = ((up_row_sum - (k1[k1_row_start - 1][k1_col_start - 1] * pwr_arr[(mid - 1) + ((mid - 1) * mid)])) * 1000) + (k1[k1_row_start - 1][k1_col_end] * pwr_arr[(mid - 1) * mid])
                    down_row_sum = ((down_row_sum - (k1[k1_row_end][k1_col_start - 1] * pwr_arr[mid - 1])) * 1000) + (k1[k1_row_end][k1_col_end] * pwr_arr[0])
                roll_hash[roll_hash_ptr] = ((roll_hash[roll_hash_ptr] - up_row_sum) * pwr_arr[mid]) + down_row_sum ; found_k1.add(roll_hash[roll_hash_ptr]) ; roll_hash_ptr += 1
                k1_col_start += 1 ; k1_col_end += 1
            k1_row_start += 1 ; k1_row_end += 1
        p_ptr, i, cm_sq_fnd = 0, mid - 1, False
        roll_hash[0] = 0
        while (i >= 0):
            j = mid - 1
            while (j >= 0):
                roll_hash[0] += k2[i][j] * pwr_arr[p_ptr] ; p_ptr += 1 ; j -= 1
            i -= 1
        if (roll_hash[0] in found_k1):
            cm_sq_fnd = True
        if (not cm_sq_fnd):
            k2_col_start, k2_col_end, k = 1, mid, 1
            while (k2_col_end < y):
                row, l_side_sum, r_side_sum, l_pwr_ptr, r_pwr_ptr = mid - 1, 0, 0, mid - 1, 0
                while (row >= 0):
                    l_side_sum += k2[row][k2_col_start - 1] * pwr_arr[l_pwr_ptr] ; r_side_sum += k2[row][k2_col_end] * pwr_arr[r_pwr_ptr]
                    l_pwr_ptr += mid ; r_pwr_ptr += mid ; row -= 1
                roll_hash[k] = ((roll_hash[k - 1] - l_side_sum) * 1000) + r_side_sum
                if (roll_hash[k] in found_k1):
                    cm_sq_fnd = True ; break
                k += 1 ; k2_col_start += 1 ; k2_col_end += 1
        if (not cm_sq_fnd):
            k2_row_start, k2_row_end = 1, mid
            while (k2_row_end < x):
                k2_col_start, k2_col_end = 0, mid - 1
                up_row_sum, down_row_sum, roll_hash_ptr = 0, 0, 0
                while (k2_col_end < y):
                    if (k2_col_start == 0):
                        k = 1
                        for i in range(k2_col_start, k2_col_end + 1):
                            up_row_sum += k2[k2_row_start - 1][i] * pwr_arr[(mid - k) + ((mid - 1) * mid)]
                            down_row_sum += k2[k2_row_end][i] * pwr_arr[(mid - k)] ; k += 1
                    else:
                        up_row_sum = ((up_row_sum - (k2[k2_row_start - 1][k2_col_start - 1] * pwr_arr[(mid - 1) + ((mid - 1) * mid)])) * 1000) + (k2[k2_row_start - 1][k2_col_end] * pwr_arr[(mid - 1) * mid])
                        down_row_sum = ((down_row_sum - (k2[k2_row_end][k2_col_start - 1] * pwr_arr[mid - 1])) * 1000) + (k2[k2_row_end][k2_col_end] * pwr_arr[0])
                    roll_hash[roll_hash_ptr] = ((roll_hash[roll_hash_ptr] - up_row_sum) * pwr_arr[mid]) + down_row_sum
                    if (roll_hash[roll_hash_ptr] in found_k1):
                        cm_sq_fnd = True ; break
                    roll_hash_ptr += 1
                    k2_col_start += 1 ; k2_col_end += 1
                if (cm_sq_fnd):
                    break
                k2_row_start += 1 ; k2_row_end += 1
        if (cm_sq_fnd):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
        found_k1.clear()
    sys.stdout.write(str(ans) + '\n')

size_of_bcs()