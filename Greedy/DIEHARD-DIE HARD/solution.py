import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def diehard ():
    T = int(input().decode())
    for t in range(T):
        H, A = map(int, input().decode().split(' ')) ; time = 0
        while (True):
            if ((time % 2) == 0): H, A = (H + 3), (A + 2)
            else:
                if ((H > 5) and (A > 10)): H, A = (H - 5), (A - 10)
                else: H, A = (H - 20), (A + 5)
            if ((H <= 0) or (A <= 0)): break
            time += 1
        sys.stdout.write(str(time) + '\n')

diehard()
