import io, os, sys, math
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def eko ():
    N, M = map(int, input().decode().split(' '))
    height_arr = input().decode().split(' ') ; right = 0
    for i in range(N):
        num = int(height_arr[i]) ; height_arr[i] = num
        if (num > right): right = num
    left, height = 0, 0
    while (left <= right):
        mid = left + ((right - left) // 2) ; woods = 0 ; i = 0
        while (i < N):
            if (height_arr[i] > mid): woods += height_arr[i] - mid
            i += 1
        if (woods == M):
            height = mid ; break
        elif (woods > M):
            height = mid if (mid > height) else height
            left = mid + 1
        else:
            right = mid - 1
    sys.stdout.write(str(height) + '\n')

eko()
