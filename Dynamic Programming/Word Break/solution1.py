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
    def __word_break_helper (self, i, line):
        if (i == len(line)): return True
        if (self.dp[i] == None):
            self.dp[i] = False
            ptr = self.dct_trie.root
            for j in range(i, len(line)):
                if (line[j] not in ptr.children): break
                ptr = ptr.children[line[j]]
                if (ptr.is_end):
                    if (self.__word_break_helper(j + 1, line)):
                        self.dp[i] = True ; break
        return self.dp[i]

    def wordBreak (self, line, dictionary):
        self.dp = [None for i in range(len(line) + 1)]
        self.dct_trie = Trie()
        for word in dictionary: self.dct_trie.insert(word)
        return self.__word_break_helper(0, line)
