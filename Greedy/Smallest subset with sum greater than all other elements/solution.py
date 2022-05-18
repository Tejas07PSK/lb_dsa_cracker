class Solution:
    def minSubset (self, arr, N):
        add_tot, curr_sum, curr_count = sum(arr), 0, 0
        arr.sort(reverse=True)
        for i in range(N):
            curr_sum += arr[i] ; curr_count += 1
            if (curr_sum > (add_tot - curr_sum)): return curr_count
        return curr_count
