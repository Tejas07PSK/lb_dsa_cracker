# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class BST:
    def search (self, root, key):
        if (root == None): return False
        if (key == root.data): return True
        elif ((key < root.data) and (root.left != None)): return self.search(root.left, key)
        elif ((key > root.data) and (root.right != None)): return self.search(root.right, key)
        return False
