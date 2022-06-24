from math import inf
class Solution:
    def __tugOfWarHelper (self, arr, n, hf_sz, prev_idx, curr_tot):
        if (hf_sz == 0):
            curr_diff = abs((2 * curr_tot) - self.tot)
            if (curr_diff < self.res):
                self.res = curr_diff
                ptr1, ptr2 = 0, 0
                for j in range(n):
                    if (j in self.res_tmp_idx_set):
                        self.res_arrs[0][ptr1] = arr[j]
                        ptr1 += 1
                    else:
                        self.res_arrs[1][ptr2] = arr[j]
                        ptr2 += 1
            return
        for i in range(prev_idx, (n - hf_sz + 1)):
            self.res_tmp_idx_set.add(i)
            self.__tugOfWarHelper(arr, n, hf_sz - 1, i + 1, curr_tot + arr[i])
            self.res_tmp_idx_set.discard(i)

    def tugOfWar (self, arr, n):
        self.tot, self.hf_sz, self.res = sum(arr), ((n + 1) // 2), inf
        self.res_tmp_idx_set = set()
        self.res_arrs = [[None for i in range(self.hf_sz)], [None for j in range(n - self.hf_sz)]]
        self.__tugOfWarHelper(arr, n, self.hf_sz, 0, 0)
        return self.res_arrs
