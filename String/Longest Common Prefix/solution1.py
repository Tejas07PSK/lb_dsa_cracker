class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        n = len(strs)
        if (n == 1):
            return strs[0]
        l = len(strs[0])
        i = 0
        while (i < l):
            j = 1
            while ((j < n) and (i < len(strs[j])) and (strs[j][i] == strs[j - 1][i])):
                j += 1
            if (j < n):
                break
            i += 1
        return strs[0][0:i]
