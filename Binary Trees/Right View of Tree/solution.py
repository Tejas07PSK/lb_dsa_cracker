'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
class Solution:
    def rightView (self, root):
        if (root == None): return []
        rv, q, q_size = deque(), deque(), 1
        q.append(root)
        while (q):
            nxt_lvl_cnt = 0 ; rv.append(None)
            while (q_size > 0):
                tree_node = q.popleft() ; q_size -= 1
                rv[-1] = tree_node.data
                if (tree_node.left != None):
                    q.append(tree_node.left) ; nxt_lvl_cnt += 1
                if (tree_node.right != None):
                    q.append(tree_node.right) ; nxt_lvl_cnt += 1
            q_size = nxt_lvl_cnt
        return rv
