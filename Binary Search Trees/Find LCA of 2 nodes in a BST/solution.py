# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

def __searchHelper (node, key):
    if (node.data == key): return True, node
    elif (key < node.data): return False, node.left
    else: return False, node.right

def LCA (root, key1, key2):
    if (root == None): return root
    found_1, found_2 = False, False
    ptr_1, ptr_2 = root, root
    lca_node = None
    while (((ptr_1 != None) and (ptr_2 != None)) and ((not found_1) or (not found_2))):
        if (ptr_1 == ptr_2): lca_node = ptr_1
        if (not found_1): found_1, ptr_1 = __searchHelper(ptr_1, key1)
        if (not found_2): found_2, ptr_2 = __searchHelper(ptr_2, key2)
    return lca_node if (found_1 and found_2) else root
