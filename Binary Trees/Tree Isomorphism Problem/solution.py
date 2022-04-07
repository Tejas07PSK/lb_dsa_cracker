'''
class Node:
    def __init__ (self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def isIsomorphic (self, root_a, root_b):
        if ((root_a == None) and (root_b == None)): return True
        if ((root_a == None) or (root_b == None)): return False
        if (root_a.data != root_b.data): return False
        if (not self.isIsomorphic(root_a.left, root_b.left)):
            if (not self.isIsomorphic(root_a.left, root_b.right)): return False
        if (not self.isIsomorphic(root_a.right, root_b.right)):
            if (not self.isIsomorphic(root_a.right, root_b.left)): return False
        return True
