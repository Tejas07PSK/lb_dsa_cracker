class TrieNode:
    def __init__(self):
        self.char_child_map = {}
        self.is_a_word = False

class Solution:
    def longestCommonPrefix (self, strs: List[str]) -> str:
        n = len(strs)
        if (n == 0):
            return ""
        if (n == 1):
            return strs[0]
        if (strs[0] == ""):
            return ""
        root = TrieNode()
        for string in strs:
            current = root
            for ch in string:
                if (ch not in current.char_child_map):
                    if ((current == root) and (len(current.char_child_map) == 1)):
                        return ""
                    current.char_child_map[ch] = TrieNode()
                current = current.char_child_map[ch]
            current.is_a_word = True
        res = []
        current = root
        while ((len(current.char_child_map) == 1) and (not current.is_a_word)):
            for ch, loc in current.char_child_map.items():
                res.append(ch)
                current = loc
        return "".join(res)
