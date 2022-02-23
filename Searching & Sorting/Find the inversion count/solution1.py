class Solution:
    def __init__ (self):
        self.__inv_cnt = 0

    def inversionCount (self, arr, n):
        self.__enhcMergeSort(0, (n - 1), arr)
        return self.__inv_cnt

    def __enhcMergeSort(self, left, right, arr):
        size = right - left + 1
        if (size < 2): return
        if (size == 2):
            if (arr[left] > arr[right]):
                self.__inv_cnt += 1
                arr[left], arr[right] = arr[right], arr[left]
            return
        mid = left + ((right - left) // 2)
        self.__enhcMergeSort(left, mid, arr) ; self.__enhcMergeSort((mid + 1), right, arr)
        self.__enhcMerge(left, mid, right, arr)

    def __enhcMerge(self, left, mid, right, arr):
        tmp_arr = [0 for i in range(left, (right + 1))] ; i, j, cntr = left, (mid + 1), 0
        while ((i <= mid) and (j <= right)):
            if (arr[i] > arr[j]):
                tmp_arr[cntr] = arr[j] ; j += 1 ; self.__inv_cnt += 1
            elif (arr[i] < arr[j]):
                tmp_arr[cntr] = arr[i] ; i += 1
            else:
                tmp_arr[cntr] = arr[i] ; i += 1 ; cntr += 1
                tmp_arr[cntr] = arr[j] ; j += 1
            cntr += 1
        while (i <= mid):
            tmp_arr[cntr] = arr[i] ; i += 1 ; cntr += 1 ; self.__inv_cnt += 1
        while (j <= right):
            tmp_arr[cntr] = arr[j] ; j += 1 ; cntr += 1
        i, cntr = left, 0
        while (i <= right):
            arr[i] = tmp_arr[cntr] ; i += 1 ; cntr += 1

        