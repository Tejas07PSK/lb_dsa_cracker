import io, os, sys, bisect
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
 
def subset_sum_in_range ():
    n, a, b = map(int, input().decode().split()) ; nums_arr = [int(input().decode()) for i in range(n)]
    def generate_subset_sum_array (left, right):
        size = 2 ** (right - left + 1) ; ssa = []
        for i in range(size):
            j, curr_sum = left, 0
            while ((i != 0) and (j <= right)):
                if ((i & 1) != 0): curr_sum += nums_arr[j]
                i >>= 1 ; j += 1
            ssa.append(curr_sum)
        return ssa
    mid = (n - 1) // 2 ; arr1, arr2 = generate_subset_sum_array(0, mid), generate_subset_sum_array((mid + 1), (n - 1))
    arr2.sort() ; ans = 0
    for i in range(len(arr1)):
        ans += (bisect.bisect_right(arr2, (b - arr1[i])) - bisect.bisect_left(arr2, (a - arr1[i])))
    sys.stdout.write(str(ans) + '\n')
 
subset_sum_in_range()
