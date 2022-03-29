'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def __isSumTreeHelper (self, root):
        if (root == None): return 0, True
        if ((root.left == None) and (root.right == None)): return root.data, True
        left_sum, left_state = 0, True
        right_sum, right_state = 0, True
        if (root.left != None):
            left_sum, left_state = self.__isSumTreeHelper(root.left)
            if (not left_state): return left_sum, False
        if (root.right != None):
            right_sum, right_state = self.__isSumTreeHelper(root.right)
            if (not right_state): return right_sum, False
        add = left_sum + right_sum
        return (root.data + add, True) if (root.data == add) else (add, False)
  
    def isSumTree (self, root):
        return self.__isSumTreeHelper(root)[1]
