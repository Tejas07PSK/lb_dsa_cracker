import math
class Solution:
    def dp (self, nums, i, n, k, memo):
        if (i == n - 1):
            if (memo[i] == math.inf):
                memo[i] = 0
            return memo[i]
        if (memo[i] != math.inf):
            return memo[i]
        min_so_far = math.inf
        sum_of_words = 0
        for j in range(i, n):
            sum_of_words += nums[j]
            if ((sum_of_words + (j - i)) <= k):
                temp = 0
                if (j < (n - 1)):
                    temp = (((k - (sum_of_words + (j - i))) ** 2) + (self.dp(nums, (j + 1), n, k, memo)))
                min_so_far = min(min_so_far, temp)
            else:
                break
        memo[i] = min_so_far
        return memo[i]

    def solveWordWrap (self, nums, k):
        n = len(nums)
        memo = [math.inf for j in range(n)]
        return self.dp(nums, 0, n, k, memo)
