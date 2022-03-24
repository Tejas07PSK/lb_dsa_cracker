'''
class Node:
    def __init__ (self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque
class Solution:
    def printBoundaryView (self, root):
        if (root == None): return []
        res, stk = deque(), deque()
        res.append(root.data)
        if (root.left != None):
            stk.append((root.left, 0))
            while (stk):
                tree_node, curr_diag = stk.pop()
                if ((curr_diag == 0) or ((tree_node.left == None) and (tree_node.right == None))): res.append(tree_node.data)
                if (tree_node.right != None): stk.append((tree_node.right, curr_diag if (tree_node.left == None) else curr_diag + 1))
                if (tree_node.left != None): stk.append((tree_node.left, curr_diag))
        if (root.right != None):
            other_res = deque()
            stk.append((root.right, 0))
            while (stk):
                tree_node, curr_diag = stk.pop()
                if ((curr_diag == 0) or ((tree_node.left == None) and (tree_node.right == None))): other_res.appendleft(tree_node.data)
                if (tree_node.left != None): stk.append((tree_node.left, curr_diag if (tree_node.right == None) else curr_diag + 1))
                if (tree_node.right != None): stk.append((tree_node.right, curr_diag))
            res.extend(other_res)
        return res
