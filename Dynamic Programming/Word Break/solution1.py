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
    def __word_break_helper (self, i, j, ptr, line):
        if (j == len(line)): return True if (i == len(line)) else False
        if (self.dp[i][j] == None):
            self.dp[i][j] = False
            if (line[j] in ptr.children):
                ptr = ptr.children[line[j]]
                if (ptr.is_end): self.dp[i][j] = self.__word_break_helper(j + 1, j + 1, self.dct_trie.root, line)
                if (not self.dp[i][j]): self.dp[i][j] = self.__word_break_helper(i, j + 1, ptr, line)
        return self.dp[i][j]

    def wordBreak (self, line, dictionary):
        self.dp = [[None for i in range(len(line) + 1)] for j in range(len(line) + 1)]
        self.dct_trie = Trie()
        for word in dictionary: self.dct_trie.insert(word)
        return self.__word_break_helper(0, 0, self.dct_trie.root, line)
