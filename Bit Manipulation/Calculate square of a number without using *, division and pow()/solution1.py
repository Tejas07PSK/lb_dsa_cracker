def calculateSquare (n):
    if (n == 0): return 0
    if (n < 0): n = -n
    if ((n & 1) == 1):
        return ((calculateSquare(n >> 1) << 2) + ((n >> 1) << 2) + 1)
    else: return (calculateSquare(n >> 1) << 2)
