import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def gergovia ():
    while (True):
        n = int(input().decode())
        if (n == 0): break
        lst = list(map(int, input().decode().split(' ')))
        i, j, work = 0, 0, 0
        while ((i < n) and (j < n)):
            if (lst[i] <= 0): i += 1
            elif (lst[j] >= 0): j += 1
            else:
                lesser = min(lst[i], -lst[j])
                work += (abs(j - i) * lesser)
                lst[i] -= lesser ; lst[j] += lesser
        sys.stdout.write(str(work) + '\n')

gergovia()
