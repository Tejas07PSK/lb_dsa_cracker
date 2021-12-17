class Solution:
    def nextPermutation (self, N, arr):
        i, j = N - 1, N - 1
        while ((i > 0) and (arr[i] <= arr[i - 1])):
            i -= 1
        i -= 1
        if (i >= 0):
            while ((j >= 0) and (arr[j] <= arr[i])):
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
            j = N - 1
        i += 1
        while (i < j):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1 ; j -= 1
        return arr
