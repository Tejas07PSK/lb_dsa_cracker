'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def diameter (self, root):
        if (root == None): return 0
        return self.diameterHelper(root)[1]

    def diameterHelper (self, root):
        hl, dl = 0, 1
        hr, dr = 0, 1
        if (root.left != None): hl, dl = self.diameterHelper(root.left)
        if (root.right != None): hr, dr = self.diameterHelper(root.right)
        return (max(hl, hr) + 1), max((hl + hr + 1), dl, dr)
