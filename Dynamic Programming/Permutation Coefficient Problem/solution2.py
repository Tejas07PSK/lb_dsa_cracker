def P (n, k):
    if (k > n): return 0
    if (k == 0): return 1
    md, f, i = 1000000007, 1, 0
    while (i < k):
        f = (f * (n - i)) % md
        i += 1
    return f
