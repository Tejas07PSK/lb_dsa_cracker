"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

#Function to insert string into TRIE.
def insert (root, key):
    for ch in key:
        ch_idx = ord(ch) - ord('a')
        if (root.children[ch_idx] == None): root.children[ch_idx] = TrieNode()
        root = root.children[ch_idx]
    root.isEndOfWord = True

#Function to use TRIE data structure and search the given string.
def search (root, key):
    for ch in key:
        ch_idx = ord(ch) - ord('a')
        if (root.children[ch_idx] == None): return False
        root = root.children[ch_idx]
    return root.isEndOfWord
