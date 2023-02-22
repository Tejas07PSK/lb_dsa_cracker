def calculateSquare (n):
    if (n == 0): return 0
    if (n < 0): n = -n
    ans, tmp_n = 0, n
    while (tmp_n > 0):
        x, pwr_2 = 0, 1
        while (pwr_2 <= tmp_n):
            pwr_2 <<= 1
            x += 1
        x -= 1
        ans += (n << x)
        pwr_2 = pwr_2 if (pwr_2 == 1) else (pwr_2 >> 1)
        tmp_n -= pwr_2
    return ans
