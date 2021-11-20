def countElementsLeK (arr, k):
    nlek = 0
    for num in arr:
        if (num <= k):
            nlek += 1
    return nlek

def minSwap (arr, n, k):
    win_len = countElementsLeK(arr, k)
    if ((win_len == 0) or (win_len == n)):
        return 0
    l, congtkinw = 0, 0
    for i in range(win_len):
        congtkinw += 1 if (arr[i] > k) else 0
    l, r = 0, win_len
    res = congtkinw
    while (r < n):
        congtkinw -= 1 if (arr[l] > k) else 0
        congtkinw += 1 if (arr[r] > k) else 0
        res = min(res, congtkinw)
        l += 1
        r += 1
    return res
