import math
class Solution:
    def preparePossibleCostsMatrix (self, nums, n, k):
        i, mat = 0, [[math.inf for j in range(n)] for i in range(n)]
        while (i < n):
            j, sum_so_far = i, 0
            while (j < n):
                sum_so_far += nums[j]
                if ((sum_so_far + (j - i)) <= k):
                    mat[i][j] = ((k - (sum_so_far + (j - i))) ** 2) if (j < (n - 1)) else 0
                else:
                    break
                j += 1
            i += 1
        return mat

    def solveWordWrap (self, nums, k):
        n = len(nums)
        possible_costs_mat = self.preparePossibleCostsMatrix(nums, n, k)
        #print(possible_costs_mat)
        dp = [inf for i in range(n)]
        #arrangement = [inf for i in range(n)]
        dp[n - 1] = 0
        i = n - 2
        while (i >= 0):
            j = n - 1
            while ((possible_costs_mat[i][j] == math.inf) and (possible_costs_mat[i][j - 1] == math.inf)):
                j -= 1
            dp[i] = possible_costs_mat[i][j]
            #arrangement[i] = j
            while (j > i):
                temp = possible_costs_mat[i][j - 1] + dp[j]
                if (temp < dp[i]):
                    dp[i] = temp
                    #arrangement[i] = j
                j -= 1
            i -= 1
        #print(dp)
        #print(arrangement)
        return (dp[0])
