class TrieNode:
    def __init__ (self):
        self.children = {}
        self.freq = 0

class Solution:
    def findPrefixes (self, arr, N):
        root = TrieNode()
        for word in arr:
            ptr = root
            for ch in word:
                if (ch not in ptr.children): ptr.children[ch] = TrieNode()
                ptr = ptr.children[ch] ; ptr.freq += 1
        res, count = ["" for i in range(N)], 0
        for word in arr:
            tmp_str, ptr = [], root
            for ch in word:
                ptr = ptr.children[ch]
                tmp_str.append(ch)
                if (ptr.freq == 1):
                    res[count] = "".join(tmp_str)
                    count += 1
                    break
        return res
