class Solution:
    def __inversion_count_helper (self, l, r, arr):
        sz = r - l + 1
        if (sz < 2): return
        if (sz == 2):
            if (arr[l] > arr[r]):
                arr[l], arr[r] = arr[r], arr[l]
                self.inv_cnt += 1
            return
        else:
            mid = l + ((r - l) // 2)
            self.__inversion_count_helper(l, mid, arr)
            self.__inversion_count_helper(mid + 1, r, arr)
            self.__merge(l, mid, mid + 1, r, arr)

    def __merge (self, l1, r1, l2, r2, arr):
        tmp_arr1 = [arr[i] for i in range(l1, r1 + 1)]
        tmp_arr2 = [arr[i] for i in range(l2, r2 + 1)]
        i, j, cntr = 0, 0, l1
        while ((i < len(tmp_arr1)) and (j < len(tmp_arr2))):
            if (tmp_arr1[i] > tmp_arr2[j]):
                arr[cntr] = tmp_arr2[j]
                cntr += 1 ; j += 1
            else:
                self.inv_cnt += j
                arr[cntr] = tmp_arr1[i]
                cntr += 1 ; i += 1
        while (i < len(tmp_arr1)):
            self.inv_cnt += j
            arr[cntr] = tmp_arr1[i]
            cntr += 1 ; i += 1
        while (j < len(tmp_arr2)):
            arr[cntr] = tmp_arr2[j]
            cntr += 1 ; j += 1

    def inversionCount (self, arr, n):
        self.inv_cnt = 0
        self.__inversion_count_helper(0, n - 1, arr)
        return self.inv_cnt
