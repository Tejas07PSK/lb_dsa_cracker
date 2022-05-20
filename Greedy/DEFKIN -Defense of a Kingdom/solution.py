import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def defkin ():
    T = int(input().decode())
    for t in range(T):
        w, h, n = map(int, input().decode().split(' '))
        if (n == 0):
            sys.stdout.write(str(w * h) + '\n') ; continue
        coords = [tuple(map(int, input().decode().split(' '))) for i in range(n)]
        coords.sort(key=lambda x: x[0])
        max_empty_width, l = (coords[0][0] - 1), (coords[0][0] + 1)
        for i in range(1, n): max_empty_width, l = max(max_empty_width, (coords[i][0] - l)), (coords[i][0] + 1)
        max_empty_width = max(max_empty_width, ((w + 1) - l))
        coords.sort(key=lambda y: y[1])
        max_empty_height, m = (coords[0][1] - 1), (coords[0][1] + 1)
        for i in range(1, n): max_empty_height, m = max(max_empty_height, (coords[i][1] - m)), (coords[i][1] + 1)
        max_empty_height = max(max_empty_height, ((h + 1) - m))
        sys.stdout.write(str(max_empty_width * max_empty_height) + '\n')

defkin()
