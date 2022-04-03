'''
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __dfs_helper (self, root):
        if (root == None): return 0, 0
        max_sum_left, max_sum_right = 0, 0
        max_sum_left_below, max_sum_right_below = 0, 0
        if (root.left != None):
            max_sum_left, max_sum_left_below = self.__dfs_helper(root.left)
        if (root.right != None):
            max_sum_right, max_sum_right_below = self.__dfs_helper(root.right)
        return max((root.data + max_sum_left_below + max_sum_right_below), (max_sum_left + max_sum_right)), (max_sum_left + max_sum_right)

    def getMaxSum (self, root):
        return self.__dfs_helper(root)[0]
