'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    def __bToDLLHelper (self, root):
        head, tail = root, root
        if (root == None): return head, tail
        if (root.left != None):
            head, tmp_tail = self.__bToDLLHelper(root.left)
            tmp_tail.right, root.left = root, tmp_tail
        if (root.right != None):
            tmp_head, tail = self.__bToDLLHelper(root.right)
            root.right, tmp_head.left = tmp_head, root
        return head, tail

    def bToDLL (self, root):
        return self.__bToDLLHelper(root)[0]
