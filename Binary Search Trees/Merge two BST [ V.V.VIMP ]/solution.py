'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque
class BinaryTreeInOrderIterator:
    def __init__ (self, root):
        self.stk = deque()
        if (root != None):
            self.stk.append(root)
            while (self.stk[-1].left != None): self.stk.append(self.stk[-1].left)

    def hasNext(self): return True if (self.stk) else False

    def getNext(self):
        res = None
        if (self.hasNext()):
            res = self.stk.pop()
            if (res.right != None):
                self.stk.append(res.right)
                while (self.stk[-1].left != None): self.stk.append(self.stk[-1].left)
        return res

class Solution:
    def merge (self, root1, root2):
        itr1, itr2 = BinaryTreeInOrderIterator(root1), BinaryTreeInOrderIterator(root2)
        ptr1, ptr2, res = itr1.getNext(), itr2.getNext(), []
        while ((ptr1 != None) and (ptr2 != None)):
            if (ptr1.data < ptr2.data):
                res.append(ptr1.data) ; ptr1 = itr1.getNext()
            else:
                res.append(ptr2.data) ; ptr2 = itr2.getNext()
        if (ptr1 != None): res.append(ptr1.data)
        if (ptr2 != None): res.append(ptr2.data)
        while (itr1.hasNext()): res.append(itr1.getNext().data)
        while (itr2.hasNext()): res.append(itr2.getNext().data)
        return res
