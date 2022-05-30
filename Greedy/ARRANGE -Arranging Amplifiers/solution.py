import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def arrange ():
    T = int(input().decode())
    for t in range(T):
        n = int(input().decode())
        arr = list(map(int, input().decode().split(' ')))
        arr.sort() ; i = 0
        while ((i < n) and (arr[i] == 1)): i += 1
        if (((i + 2) == n) and (arr[i] == 2) and (arr[i + 1] == 3)): pass
        else:
            j = n - 1
            while (i < j):
                arr[i], arr[j] = arr[j], arr[i]
                i, j =  i + 1, j - 1
        i = 0
        while (i < n):
            if (i != n - 1): sys.stdout.write(str(arr[i]) + ' ')
            else: sys.stdout.write(str(arr[i]) + '\n')
            i += 1

arrange()
