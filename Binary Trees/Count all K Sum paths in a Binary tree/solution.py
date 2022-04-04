'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

factor = 10 ** 9 + 7
class Solution:
    def __dfs_helper (self, sum_top_down, root, k):
        if ((sum_top_down - k) in self.seen): self.count += self.seen[(sum_top_down - k)]
        if (sum_top_down not in self.seen): self.seen[sum_top_down] = 1
        else: self.seen[sum_top_down] += 1
        if (root.left != None): self.__dfs_helper((sum_top_down + root.left.data), root.left, k)
        if (root.right != None): self.__dfs_helper((sum_top_down + root.right.data), root.right, k)
        if (self.seen[sum_top_down] == 1): del self.seen[sum_top_down]
        else: self.seen[sum_top_down] -= 1

    def sumK (self, root, k):
        if (root == None): return 0
        self.seen, self.count = {}, 0 ; self.seen[0] = 1
        self.__dfs_helper(root.data, root, k)
        return self.count % factor
