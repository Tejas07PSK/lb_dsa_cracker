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
    def __wordBreakHelper (self, s, start):
        if (start == len(s)): return True
        if (self.dp[start] == None):
            for end in range(start, len(s)):
                if (self.tri.search(start, end, s) and self.__wordBreakHelper(s, end + 1)):
                    self.dp[start] = True
                    return True
            self.dp[start] = False
        return self.dp[start]

    def wordBreak (self, s: str, wordDict: List[str]) -> bool:
        self.tri = Trie()
        for word in wordDict: self.tri.insert(0, len(word) - 1, word)
        self.dp = [None for i in range(len(s))]
        return self.__wordBreakHelper(s, 0)
