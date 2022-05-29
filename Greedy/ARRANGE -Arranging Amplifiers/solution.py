import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def arrange ():
    T = int(input().decode())
    for t in range(T):
        input()
        m, n = map(int, input().decode().split(' '))
        m, n = (m - 1), (n - 1)
        cols = [int(input().decode()) for i in range(m)]
        rows = [int(input().decode()) for i in range(n)]
        cols.sort(reverse=True) ; rows.sort(reverse=True)
        i, j, cost = 0, 0, 0
        while ((i < m) and (j < n)):
            if (cols[i] >= rows[j]): cost, i = (cost + (cols[i] * (j + 1))), (i + 1)
            else: cost, j = (cost + (rows[j] * (i + 1))), (j + 1)
        while (i < m): cost, i = (cost + (cols[i] * (j + 1))), (i + 1)
        while (j < n): cost, j = (cost + (rows[j] * (i + 1))), (j + 1)
        sys.stdout.write(str(cost) + '\n')

arrange()