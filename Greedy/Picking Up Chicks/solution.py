import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

def pickupchicks ():
    C = int(input().decode())
    for i in range(C):
        N, K, B, T = map(int, input().decode().split(' '))
        pos_arr = list(map(int, input().decode().split(' ')))
        speed_arr = list(map(int, input().decode().split(' ')))
        count, swaps, impossibles = 0, 0, 0
        for j in range(N - 1, -1, -1):
            act_dist, possible_dist = (B - pos_arr[j]), (T * speed_arr[j])
            if (possible_dist >= act_dist):
                count += 1
                if (impossibles > 0): swaps += impossibles
            else: impossibles += 1
            if (count >= K):
                sys.stdout.write("Case #{}: {}\n".format(i + 1, swaps)) ; break
        if (count < K): sys.stdout.write("Case #{}: IMPOSSIBLE\n".format(i + 1))

pickupchicks()
