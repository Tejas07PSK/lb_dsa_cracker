class Solution:
    def findTwoElement (self, arr, n):
        if (n == 1):
            return [0, 0] if ((arr[0] == 1) or (arr[0] == 0)) else [0, 1]
        res = [0, 0]
        for i in range(n):
            if (arr[abs(arr[i]) - 1] < 0):
                res[0] = abs(arr[i])
            else:
                arr[abs(arr[i]) - 1] *= -1
        for i in range(n):
            if (arr[i] > 0):
                res[1] = i + 1
                break
        return res
