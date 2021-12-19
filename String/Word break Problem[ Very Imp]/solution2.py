class Solution:
    def wordBreak(self, sentence: str, word_list: List[str]) -> bool:
        ws, n = set(word_list), len(sentence)
        dp = [False for num in range(0, (n + 1))]
        dp[0] = True
        for i in range(1, (n + 1)):
            for j in range(0, i):
                if (dp[j] and (sentence[j:i] in ws)):
                    dp[i] = True
                    break
        return dp[n]
