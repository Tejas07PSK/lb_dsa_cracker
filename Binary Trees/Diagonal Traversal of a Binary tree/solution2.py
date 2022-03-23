'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
def diagonal (root):
    if (root == None): return []
    dg_map, nof_diags = {}, 0
    q = deque() ; q.append((root, 0))
    while (q):
        tree_node, diag = q.pop()
        if (diag > nof_diags): nof_diags = diag
        if (diag not in dg_map): dg_map[diag] = deque()
        dg_map[diag].append(tree_node.data)
        if (tree_node.right != None): q.append((tree_node.right, diag))
        if (tree_node.left != None): q.append((tree_node.left, diag + 1))
    return [ j for i in range(nof_diags + 1) for j in dg_map[i] ]
