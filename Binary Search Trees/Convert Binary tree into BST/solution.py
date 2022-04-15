'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def __inOrderHelper (self, root, mode):
        if (root.left != None): self.__inOrderHelper(root.left, mode)
        if (mode == 0): self.res_arr.append(root.data)
        else: root.data, self.i = self.res_arr[self.i], self.i + 1
        if (root.right != None): self.__inOrderHelper(root.right, mode)

    def binaryTreeToBST (self, root):
        if (root == None): return root
        self.res_arr, self.i = [], 0
        self.__inOrderHelper(root, 0) ; self.res_arr.sort()
        self.__inOrderHelper(root, 1)
        return root
