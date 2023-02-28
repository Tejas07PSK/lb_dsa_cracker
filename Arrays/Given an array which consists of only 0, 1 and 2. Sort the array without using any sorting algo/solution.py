class Solution:
    def sort012 (self, arr, n):
        i, j, k = 0, 0, n - 1
        while (j <= k):
            if (arr[j] == 0):
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
                i += 1
            elif (arr[j] == 1): j += 1
            else:
                arr[j], arr[k] = arr[k], arr[j]
                k -= 1
