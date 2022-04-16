# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

class Solution:
    def __inOrderHelper (self, root, k):
        if (root == None): return
        if (root.left != None): self.__inOrderHelper(root.left, k)
        if (self.res != None): return
        self.cntr += 1
        if (self.cntr == k):
            self.res = root.data ; return
        if (root.right != None): self.__inOrderHelper(root.right, k)

    def KthSmallestElement (self, root, k):
        self.cntr, self.res = 0, None
        self.__inOrderHelper(root, k)
        return self.res if (self.res != None) else -1
