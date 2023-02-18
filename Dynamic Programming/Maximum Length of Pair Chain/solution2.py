class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        dp = [1 for i in range(len(pairs))]
        pairs.sort(key=lambda x: x[0])
        for i in range(len(pairs) - 2, -1, -1):
            low, high = i + 1, len(pairs) - 1
            while (low <= high):
                mid = low + ((high - low) // 2)
                if (pairs[i][1] < pairs[mid][0]):
                    dp[i] = max(dp[i], 1 + dp[mid])
                    high = mid - 1
                else: low = mid + 1
            dp[i] = max(dp[i], dp[i + 1])
        return dp[0]
