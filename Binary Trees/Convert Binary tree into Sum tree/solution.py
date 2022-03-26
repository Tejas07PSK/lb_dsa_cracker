'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __toSumTreeHelper (self, root):
        curr_val = root.data ; root.data = 0
        if (root.left != None): root.data = self.__toSumTreeHelper(root.left) + root.left.data
        if (root.right != None): root.data += self.__toSumTreeHelper(root.right) + root.right.data
        return curr_val

    def toSumTree (self, root):
        if (root == None): return
        self.__toSumTreeHelper(root)
