import math
class Solution:
    def dp (self, nums, i, n, k, memo):
        if (i == n - 1):
            if (memo[i][i] == math.inf):
                memo[i][i] = 0
            return memo[i][i]
        if (memo[i][i] != math.inf):
            return memo[i][i]
        min_so_far = (((k - nums[i]) ** 2) + self.dp(nums, (i + 1), n, k, memo))
        sum_of_words = nums[i]
        for j in range((i + 1), n):
            sum_of_words += nums[j]
            if ((sum_of_words + (j - i)) <= k):
                if (j < (n - 1)):
                    memo[i][j] = (((k - (sum_of_words + (j - i))) ** 2) + (self.dp(nums, (j + 1), n, k, memo)))
                else:
                    memo[i][j] = 0
                min_so_far = min(min_so_far, memo[i][j])
            else:
                break
        memo[i][i] = min_so_far
        return memo[i][i]

    def solveWordWrap (self, nums, k):
        n = len(nums)
        memo = [[math.inf for j in range(n)] for i in range(n)]
        return self.dp(nums, 0, n, k, memo)
