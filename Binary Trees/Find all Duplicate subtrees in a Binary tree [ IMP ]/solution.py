'''
class Node:
    def __init__ (self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __dfs_duplicate_finder (self, root):
        if (root == None): return []
        left_sub_tree_list, right_sub_tree_list = [], []
        if (root.left != None): left_sub_tree_list = self.__dfs_duplicate_finder(root.left)
        if (root.right != None): right_sub_tree_list = self.__dfs_duplicate_finder(root.right)
        left_sub_tree_list.extend(right_sub_tree_list) ; left_sub_tree_list.append(str(root.data) + '|')
        tmp_str = "".join(left_sub_tree_list)
        if (tmp_str not in self.hm): self.hm[tmp_str] = 0
        elif (self.hm[tmp_str] == 0):
            self.res.append(root) ; self.hm[tmp_str] = 1
        return left_sub_tree_list

    def printAllDups (self, root):
        self.res, self.hm = [], {}
        self.__dfs_duplicate_finder(root)
        return self.res
