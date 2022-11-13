from collections import deque

class TrieNode:
    def __init__ (self):
        self.children = {}
        self.is_word_end = False

class Trie:
    def __init__ (self): self.root = TrieNode()
    def insert (self, start, end, string):
        ptr = self.root
        while (start <= end):
            if (string[start] not in ptr.children): ptr.children[string[start]] = TrieNode()
            ptr = ptr.children[string[start]]
            start += 1
        ptr.is_word_end = True
    def search (self, start, end, string):
        ptr = self.root
        while (start <= end):
            if (string[start] not in ptr.children): return False
            ptr = ptr.children[string[start]]
            start += 1
        return ptr.is_word_end

class Solution:
    def wordBreak (self, s: str, wordDict: List[str]) -> bool:
        tri = Trie()
        for word in wordDict: tri.insert(0, len(word) - 1, word)
        dp = [False for i in range(len(s) + 1)] ; dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(0, i):
                if ((dp[j] == True) and (tri.search(j, i - 1, s) == True)):
                    dp[i] = True ; break
        return dp[-1]
