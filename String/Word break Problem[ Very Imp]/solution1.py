class Solution:
    def __helper (self, sentence, ws, n, start, memo):
        if (start == n):
            return True
        if (memo[start] != None):
            return memo[start]
        for end in range((start + 1), (n + 1)):
            if ((sentence[start:end] in ws) and self.__helper(sentence, ws, n, end, memo)):
                memo[start] = True
                return (memo[start])
        memo[start] = False
        return memo[start]

    def wordBreak(self, sentence: str, word_list: List[str]) -> bool:
        ws, n = set(word_list), len(sentence)
        memo = [None for ch in sentence]
        return self.__helper(sentence, ws, n, 0, memo)
