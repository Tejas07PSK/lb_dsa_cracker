'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
class Solution:
    def height (self, root):
        if (root == None): return 0
        q = deque(); q.append(root) ; count, height = 1, 0
        while (q):
            next_lvl_nd_cnt = 0
            while (count != 0):
                tree_node = q.popleft() ; count -= 1
                if (tree_node.left != None):
                    q.append(tree_node.left) ; next_lvl_nd_cnt +=1
                if (tree_node.right != None):
                    q.append(tree_node.right) ; next_lvl_nd_cnt +=1
            count, height = next_lvl_nd_cnt, (height + 1)
        return height
