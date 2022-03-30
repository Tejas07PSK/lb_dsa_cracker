'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __checkLeafAtSameLevel (self, root, lvl):
        if (root == None): return True
        if ((root.left == None) and (root.right == None)):
            if (self.leaves_lvl == None): self.leaves_lvl = lvl
            return True if (self.leaves_lvl == lvl) else False
        if (root.left != None):
            if (not self.__checkLeafAtSameLevel(root.left, lvl + 1)): return False
        if (root.right != None):
            if (not self.__checkLeafAtSameLevel(root.right, lvl + 1)): return False
        return True

    def check (self, root):
        self.leaves_lvl = None
        return self.__checkLeafAtSameLevel(root, 0)
