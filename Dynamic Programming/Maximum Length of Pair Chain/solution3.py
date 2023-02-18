class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        ans, j = 1, 0
        pairs.sort(key=lambda x: x[1])
        for i in range(1, len(pairs)):
            if (pairs[j][1] < pairs[i][0]):
                ans += 1
                j = i
        return ans
