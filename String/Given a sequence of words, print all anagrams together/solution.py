class TrieNode:
    def __init__ (self):
        self.children = None
        self.eow = False
        self.index_list = None

class Solution:
    def __traverseTrie (self, node, result, list_of_strings):
        if (node.eow == True):
            result.append([list_of_strings[i] for i in node.index_list])
        if (node.children == None):
            return
        for tnode in node.children.values():
            self.__traverseTrie(tnode, result, list_of_strings)

    def Anagrams (self, list_of_strings, n):
        root, i = TrieNode(), 0
        for string in list_of_strings:
            itr = root
            for ch in sorted(string):
                if (itr.children == None):
                    itr.children = {}
                if ch not in itr.children:
                    itr.children[ch] = TrieNode()
                itr = itr.children[ch]
            itr.eow = True
            if (itr.index_list == None):
                itr.index_list = []
            itr.index_list.append(i)
            i += 1
        result = []
        self.__traverseTrie(root, result, list_of_strings)
        return result
