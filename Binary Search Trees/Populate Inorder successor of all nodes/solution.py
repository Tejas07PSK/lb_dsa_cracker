'''
# Binary tree node class for reference
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

in_ord_prev = None

def __populateNextHelper (root):
    global in_ord_prev
    if (root.left != None): __populateNextHelper(root.left)
    if (in_ord_prev != None): in_ord_prev.next = root ; in_ord_prev = root
    else: in_ord_prev = root
    if (root.right != None): __populateNextHelper(root.right)

def inorderSuccessor(root):
    if (root == None): return
    global in_ord_prev ; in_ord_prev = None
    __populateNextHelper(root) ; in_ord_prev.next = None
