class BIT:
    def __init__ (self, n): self.bit_arr = [0 for i in range(n + 1)]

    def summ (self, idx):
        ans = 0
        while (idx > 0):
            ans += self.bit_arr[idx]
            idx -= (idx & -idx)
        return ans

    def update (self, idx, x):
        while (idx < len(self.bit_arr)):
            self.bit_arr[idx] += x
            idx += (idx & -idx)

class Solution:
    def __compress_array (self, arr):
        hm, new_arr, cntr = {}, list(arr), 1
        new_arr.sort()
        for num in new_arr:
            if num not in hm:
                hm[num] = cntr
                cntr += 1
        for i in range(len(arr)): arr[i] = hm[arr[i]]
        return cntr - 1

    def __is_comp_req (self, arr):
        for num in arr:
            if ((num < 1) or (num > 100000)): return True
        return False

    def inversionCount (self, arr, n):
        mx = 1
        if (self.__is_comp_req(arr)): mx = self.__compress_array(arr)
        else: mx = max(arr)
        bin_idx_tree = BIT(mx) ; inv_count = 0
        for num in arr:
            inv_count += (bin_idx_tree.summ(mx) - bin_idx_tree.summ(num))
            bin_idx_tree.update(num, 1)
        return inv_count
