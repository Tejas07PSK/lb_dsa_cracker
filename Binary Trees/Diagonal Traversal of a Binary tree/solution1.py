'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque
def diagonal_helper (root, diag, dg_map, nof_diags):
    if (diag > nof_diags[0]): nof_diags[0] = diag
    if (diag not in dg_map): dg_map[diag] = deque()
    dg_map[diag].append(root.data)
    if (root.left != None): diagonal_helper(root.left, diag + 1, dg_map, nof_diags)
    if (root.right != None): diagonal_helper(root.right, diag, dg_map, nof_diags)

def diagonal (root):
    if (root == None): return []
    dg_map, nof_diags = {}, [0]
    diagonal_helper(root, 0, dg_map, nof_diags)
    return [ j for i in range(nof_diags[0] + 1) for j in dg_map[i] ]
