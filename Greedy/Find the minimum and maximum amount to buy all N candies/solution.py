class Solution:
    def candyStore (self, candies, N, K):
        candies.sort() ; i, j, cntr = 0, N - 1, 0
        ans = [0, 0]
        while (i < N):
            ans[0] += candies[i]
            while ((cntr < K) and (j > i)): j, cntr = j - 1, cntr + 1
            if (j <= i): break
            i, cntr = i + 1, 0
        i, j, cntr = N - 1, 0, 0
        while (i >= 0):
            ans[1] += candies[i]
            while ((cntr < K) and (j < i)): j, cntr = j + 1, cntr + 1
            if (j >= i): break
            i, cntr = i - 1, 0
        return ans
