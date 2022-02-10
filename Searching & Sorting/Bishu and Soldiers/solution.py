import io, os, sys
from itertools import accumulate

def number_of_soldiers_killed_per_round ():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline ; hm = {}
    n = int(input().decode()) ; sol_pwr_arr = [int(input().decode()) for i in range(n)] ; sol_pwr_arr.sort()
    index_sum_arr = list(accumulate(sol_pwr_arr)) ; rounds = int(input().decode()) ; i = 0
    while (i < rounds):
        bishu_pwr = int(input().decode())
        if bishu_pwr not in hm:
            low, high = 0, n - 1
            while (low <= high):
                mid = low + ((high - low) // 2)
                if (sol_pwr_arr[mid] <= bishu_pwr):
                    low += 1
                else:
                    high -= 1
            res = ' '.join([str(low), (str(index_sum_arr[low - 1]) + '\n') if ((low - 1) >= 0) else "0\n"])
            sys.stdout.write(res)
            hm[bishu_pwr] = res
        else:
            sys.stdout.write(hm[bishu_pwr])
        i += 1
 
number_of_soldiers_killed_per_round()
