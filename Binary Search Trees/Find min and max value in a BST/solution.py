# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

def minValue (root):
    if (root == None): return -1
    while (root.left != None): root = root.left
    return root.data
