class Solution:
    def __find_longest_chain_helper (self, i, pairs):
        if (i == len(pairs) - 1): return 1
        if (self.dp[i] == None):
            self.dp[i] = 1
            low, high = i + 1, len(pairs) - 1
            while (low <= high):
                mid = low + ((high - low) // 2)
                if (pairs[i][1] < pairs[mid][0]):
                    self.dp[i] = max(self.dp[i], 1 + self.__find_longest_chain_helper(mid, pairs))
                    high = mid - 1
                else: low = mid + 1
            self.dp[i] = max(self.dp[i], self.__find_longest_chain_helper(i + 1, pairs))
        return self.dp[i]

    def findLongestChain(self, pairs: List[List[int]]) -> int:
        self.dp = [None for i in range(len(pairs))]
        pairs.sort(key=lambda x: x[0])
        return self.__find_longest_chain_helper(0, pairs)
