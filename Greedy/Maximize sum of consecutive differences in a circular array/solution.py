def maxSum (arr, n):
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
