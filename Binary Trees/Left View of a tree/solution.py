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
    def leftView (self, root):
        if (root == None): return []
        lv, q, q_size = deque(), deque(), 1
        q.append(root)
        while (q):
            next_lvl_cnt = 0 ; lv.append(None)
            while (q_size > 0):
                tree_node = q.popleft() ; q_size -= 1
                if (lv[-1] == None): lv[-1] = tree_node.data
                if (tree_node.left != None):
                    q.append(tree_node.left) ; next_lvl_cnt += 1
                if (tree_node.right != None):
                    q.append(tree_node.right) ; next_lvl_cnt += 1
            q_size = next_lvl_cnt
        return lv
