import io, os, sys, math
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def aggressive_crows ():
    T = int(input().decode())
    for t in range(T):
        N, C = map(int, input().decode().split(' '))
        X = [int(input().decode()) for i in range(N)] ; X.sort()
        left, right, ans = 1, X[N - 1], 0
        while (left <= right):
            mid = left + ((right - left) // 2) ; rem =  C - 1 ; min_val_to_be_gt = X[0] + mid ; i = 1
            while ((rem != 0) and (i < N) and ((N - i) >= rem)):
                if (X[i] >= min_val_to_be_gt):
                    min_val_to_be_gt = X[i] + mid ; rem -= 1
                i += 1
            if (rem == 0):
                left = mid + 1 ; ans = max(ans, mid)
            else:
                right = mid - 1
        sys.stdout.write(str(ans) + '\n')

aggressive_crows()
