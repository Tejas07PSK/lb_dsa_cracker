class TrieNode:
    def __init__ (self):
        self.is_end = False
        self.char = '*'
        self.children = {}

class Trie:
    def __init__ (self): self.root = TrieNode()
    def insert (self, string):
        ptr = self.root
        for ch in string:
            if (ch not in ptr.children):
                ptr.children[ch] = TrieNode()
                ptr.children[ch].char = ch
            ptr = ptr.children[ch]
        ptr.is_end = True

class Solution:
    def wordBreak (self, line, dictionary):
        dp = [None for i in range(len(line) + 1)] ; dp[len(line)] = True
        dct_trie = Trie()
        for word in dictionary: dct_trie.insert(word)
        for i in range(len(line) - 1, -1, -1):
            dp[i] = False
            ptr = dct_trie.root
            for j in range(i, len(line)):
                if (line[j] not in ptr.children): break
                ptr = ptr.children[line[j]]
                if (ptr.is_end):
                    if (dp[j + 1]):
                        dp[i] = True ; break
        return dp[0]
