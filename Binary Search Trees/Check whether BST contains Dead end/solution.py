from math import inf
def __isDeadEndHelper (root, low, high):
    if (root == None): return False
    if (low == high): return True
    res_left, res_right = False, False
    if (root.left != None): res_left = __isDeadEndHelper(root.left, low, (root.data - 1))
    if (root.right != None): res_right = __isDeadEndHelper(root.right, (root.data + 1), high)
    return (res_left or res_right)

def isdeadEnd (root): return 1 if (__isDeadEndHelper(root, 1, inf)) else 0
