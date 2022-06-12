class Solution:
    def __wordBreakHelper(self, start, s, n):
        if (start == n): return []
        if (self.dp[start] != None): return self.dp[start]
        for end in range(start + 1, n + 1):
            prefix = s[start:end]
            if (prefix in self.set_of_words):
                rem_sen = self.__wordBreakHelper(end, s, n)
                if (rem_sen != None):
                    if (self.dp[start] == None): self.dp[start] = []
                    if (end == n): self.dp[start].append(prefix)
                    else:
                        for sen in rem_sen: self.dp[start].append(prefix + " " + sen)
        if (self.dp[start] == None): self.dp[start] = []
        return self.dp[start]

    def wordBreak (self, n, dic, s):
        n = len(s)
        self.dp, self.set_of_words = [None for i in range(n)], set(dic)
        self.__wordBreakHelper(0, s, n)
        return self.dp[0]
