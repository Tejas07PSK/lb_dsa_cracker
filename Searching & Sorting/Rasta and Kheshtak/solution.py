import io, os, sys

def size_of_bcs ():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    n, m = map(int, input().decode().split(' ')) ; k1 = [list(map(int, input().decode().split(' '))) for i in range(n)]
    x, y = map(int, input().decode().split(' ')) ; k2 = [list(map(int, input().decode().split(' '))) for j in range(x)]
    min_size = min(n, m, x, y) ; low, high, ans = 0, min_size, 0
    while (low <= high):
        mid = low + ((high - low) // 2)
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