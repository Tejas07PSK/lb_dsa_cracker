import math
class Solution:
    def solveWordWrap (self, nums, k):
        n = len(nums)
        dp = [math.inf for i in range(n)]
        dp[n - 1] = 0
        i = n - 2
        while (i >= 0):
            j = i
            sum_of_words, min_so_far = 0, math.inf
            while (j < n):
                sum_of_words += nums[j]
                if ((sum_of_words + (j - i)) <= k):
                    temp = 0
                    if (j < (n - 1)):
                        temp = ((k - (sum_of_words + (j - i))) ** 2) + dp[j + 1]
                    min_so_far = min(min_so_far, temp)
                else:
                    break
                j += 1
            dp[i] = min_so_far
            i -= 1
        return (dp[0])
