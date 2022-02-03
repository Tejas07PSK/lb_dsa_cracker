class Solution:
    def search (self, arr, n, k, key):
        i = 0
        while (i < n):
            if (arr[i] == key):
                return i
            i += max(1, (abs(key - arr[i]) // k))
        return -1
