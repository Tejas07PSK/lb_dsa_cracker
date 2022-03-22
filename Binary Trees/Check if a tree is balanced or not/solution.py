# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    def __isBalancedHelper (self, root):
        if (root == None): return -1, True
        lh, rh = -1, -1
        islb, isrb = True, True
        if (root.left != None): lh, islb = self.__isBalancedHelper(root.left)
        if (not islb): return -1, False
        if (root.right != None): rh, isrb = self.__isBalancedHelper(root.right)
        if (not isrb): return -1, False
        diff, height = lh - rh, 1 + max(lh, rh)
        return height, -1 <= diff <= 1

    def isBalanced (self, root):
        return self.__isBalancedHelper(root)[1]
