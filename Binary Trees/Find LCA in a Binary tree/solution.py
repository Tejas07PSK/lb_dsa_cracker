'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    def __dfs_helper (self, root, n1, n2):
        if (root == None): return 0
        lca_child_cntr = 0
        if ((root.data == n1) or (root.data == n2)):
            lca_child_cntr += 1; self.visited += 1 ; self.lca_node = root
        if ((self.visited != 2) and (root.left != None)):
            lca_count_from_left = self.__dfs_helper(root.left, n1, n2)
            if (lca_count_from_left == 2): return 2
            lca_child_cntr += lca_count_from_left
            if (lca_child_cntr == 2):
                self.lca_node = root ; return 2
        if ((self.visited != 2) and (root.right != None)):
            lca_count_from_right = self.__dfs_helper(root.right, n1, n2)
            if (lca_count_from_right == 2): return 2
            lca_child_cntr += lca_count_from_right
            if (lca_child_cntr == 2):
                self.lca_node = root ; return 2
        return lca_child_cntr

    def lca (self, root, n1, n2):
        self.lca_node = Node(-1) ; self.visited = 0
        self.__dfs_helper(root, n1, n2)
        return self.lca_node
