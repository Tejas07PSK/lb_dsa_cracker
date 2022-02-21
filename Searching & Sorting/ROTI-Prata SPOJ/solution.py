import io, os, sys, math
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def prata ():
    mx_lim = int(1e7)
    ap_quad_n = lambda factor, sum : int((math.sqrt((factor ** 2.0) + (4.0 * factor * sum)) - factor) / (2.0 * factor))
    T = int(input().decode())
    for t in range(T):
        P = int(input().decode()) ; tmp_nxt_ln = input().decode().split(' ')
        L, L_arr = int(tmp_nxt_ln[0]), list(map(int, tmp_nxt_ln[1:]))
        low, high, ans = 1, mx_lim, 0
        while (low <= high):
            mid = low + ((high - low) >> 1) ; count = 0
            for i in range(L):
                count += ap_quad_n((L_arr[i] / 2.0), mid)
                if (count >= P): break
            if (count < P): low = mid + 1
            else:
                high = mid - 1 ; ans = mid
        sys.stdout.write(str(ans) + '\n')

prata()