class Solution:
    def subArrayExists (self, arr, n):
        seen = set()
        sum = 0
        for i in range(0,n):
            if (arr[i] == 0):
                return True
            sum += arr[i]
            if ((sum == 0) or (sum in seen)):
                return True
            seen.add(sum)
        return False