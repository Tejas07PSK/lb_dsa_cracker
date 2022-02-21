import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def double_helix ():
    while True:
        tmp_ln_1 = input().decode().strip().split()
        if ((len(tmp_ln_1) == 0) or (tmp_ln_1[0] == "0")): break
        tmp_ln_2 = input().decode().strip().split()
        arr1, arr2 = list(map(int, tmp_ln_1[1:])), list(map(int, tmp_ln_2[1:]))
        n, m = int(tmp_ln_1[0]), int(tmp_ln_2[0])
        i, j, sum_bef_i, sum_bef_j, ovr_mx = 0, 0, 0, 0, 0
        while ((i < n) and (j < m)):
            if (arr2[j] < arr1[i]):
                sum_bef_j += arr2[j] ; j += 1
            elif (arr2[j] > arr1[i]):
                sum_bef_i += arr1[i] ; i += 1
            else:
                ovr_mx += max((sum_bef_i + arr1[i]), (sum_bef_j + arr2[j]))
                sum_bef_i, sum_bef_j = 0, 0 ; i += 1 ; j += 1
        while (i < n):
            sum_bef_i += arr1[i] ; i += 1
        while (j < m):
            sum_bef_j += arr2[j] ; j += 1
        ovr_mx += max(sum_bef_i, sum_bef_j)
        sys.stdout.write(str(ovr_mx) + '\n')

double_helix()