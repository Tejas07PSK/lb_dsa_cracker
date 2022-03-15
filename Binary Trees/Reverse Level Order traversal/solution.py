'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
def reverseLevelOrder (root):
    if (root == None): return []
    res, q = [], deque()
    q.append(root)
    while (q):
        tree_node = q.popleft()
        res.append(tree_node.data)
        if (tree_node.right != None): q.append(tree_node.right)
        if (tree_node.left != None): q.append(tree_node.left)
    res.reverse()
    return res
