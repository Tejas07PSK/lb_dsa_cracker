import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def maxAbsSum (arr, n):
    arr.sort()
    i, j, flip_flop, ans = 0, n - 1, 0, 0
    while (i < j):
        if (flip_flop == 0):
            ans += abs(arr[i] - arr[j])
            i += 1 ; flip_flop = 1
        else:
            ans += abs(arr[j] - arr[i])
            j -= 1 ; flip_flop = 0
    ans += abs(arr[j] - arr[0])
    return ans

def main ():
    t = int(input().decode())
    for i in range(t):
        n, arr = int(input().decode()), list(map(int, input().decode().strip().split()))
        sys.stdout.write(str(maxAbsSum(arr, n)) + '\n')

main()
