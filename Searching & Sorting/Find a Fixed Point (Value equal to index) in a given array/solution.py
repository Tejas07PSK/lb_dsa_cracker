class Solution:
    def valueEqualToIndex (self, arr, n):
        return [(i + 1) for i in range(n) if ((i + 1) == arr[i])]
