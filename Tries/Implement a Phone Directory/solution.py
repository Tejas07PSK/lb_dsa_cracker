class TrieNode:
    def __init__ (self):
        self.children, self.is_word_end = {}, False

class Trie:
    def __init__ (self): self.root = TrieNode()
    def insert (self, word):
        ptr = self.root
        for ch in word:
            if (ch not in ptr.children): ptr.children[ch] = TrieNode()
            ptr = ptr.children[ch]
        ptr.is_word_end = True
    def find_next_char_node (self, ptr, ch):
        if (ch not in ptr.children): return None
        return ptr.children[ch]

class Solution:
    def __dfs_over_trie(self, ptr, tmp_str, tmp_lst):
        if (ptr.is_word_end): tmp_lst.append("".join(tmp_str))
        if (not ptr.children): return
        for ch, node in ptr.children.items():
            tmp_str.append(ch)
            self.__dfs_over_trie(node, tmp_str, tmp_lst)
            tmp_str.pop()
    def displayContacts (self, n, contact, s):
        tri = Trie()
        for word in contact: tri.insert(word)
        res = [[0] for ch in s]
        tmp_str, ptr, count = [], tri.root, 0
        for ch in s:
            ptr = tri.find_next_char_node(ptr, ch)
            if (ptr == None): break
            tmp_lst = [] ; tmp_str.append(ch)
            self.__dfs_over_trie(ptr, tmp_str, tmp_lst)
            tmp_lst.sort()
            res[count] = tmp_lst ; count += 1
        return res
