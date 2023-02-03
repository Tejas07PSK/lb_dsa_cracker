class Solution:
    def AlternatingaMaxLength (self, arr):
        dec, inc = 1, 1
        for i in range(len(arr) - 2, -1, -1):
            if (arr[i] > arr[i + 1]): inc = dec + 1
            if (arr[i] < arr[i + 1]): dec = inc + 1
        return max(inc, dec)
