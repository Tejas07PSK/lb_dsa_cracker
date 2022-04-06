'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    def __dfs_helper (self, root, a, b):
        if (root == None): return 0, 0
        lca_child_count, dist = 0, 0
        if ((root.data == a) or (root.data == b)):
            self.visited += 1 ; lca_child_count += 1
        if ((self.visited != 2) and (root.left != None)):
            lca_child_count_left, dist_left = self.__dfs_helper(root.left, a, b)
            lca_child_count += lca_child_count_left
            if (lca_child_count_left == 1): dist += dist_left + 1
            else: dist += dist_left
        if ((self.visited != 2) and (root.right != None)):
            lca_child_count_right, dist_right = self.__dfs_helper(root.right, a, b)
            lca_child_count += lca_child_count_right
            if (lca_child_count_right == 1): dist += dist_right + 1
            else: dist += dist_right
        return lca_child_count, dist

    def findDist (self, root, a, b):
        self.visited = 0 ; dist  = self.__dfs_helper(root, a, b)[1]
        return -1 if (self.visited < 2) else dist
