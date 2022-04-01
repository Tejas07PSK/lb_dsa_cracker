'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def __helper (self, root, sum_so_far, path_len):
        if ((root.left == None) and (root.right == None)):
            if ((path_len > self.max_len) or ((path_len == self.max_len) and (sum_so_far > self.max_sum))):
                self.max_len, self.max_sum = path_len, sum_so_far
            return
        if (root.left != None): self.__helper(root.left, sum_so_far + root.left.data, path_len + 1)
        if (root.right != None): self.__helper(root.right, sum_so_far + root.right.data, path_len + 1)

    def sumOfLongRootToLeafPath (self, root):
        if (root == None): return 0
        self.max_len, self.max_sum = 0, 0
        self.__helper(root, root.data, 0)
        return self.max_sum
