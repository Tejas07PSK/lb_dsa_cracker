'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

from collections import deque
class BinaryTreeInOrderIterator:
    def __init__ (self, root, reverse=False):
        self.stk, self.reverse = deque(), reverse
        if (root != None):
            self.stk.append(root)
            if (self.reverse):
                while (self.stk[-1].right != None): self.stk.append(self.stk[-1].right)
            else:
                while (self.stk[-1].left != None): self.stk.append(self.stk[-1].left)

    def getNext (self):
        res = None
        if (self.stk):
            res = self.stk.pop()
            if (self.reverse):
                if (res.left != None):
                    self.stk.append(res.left)
                    while (self.stk[-1].right != None): self.stk.append(self.stk[-1].right)
            else:
                if (res.right != None):
                    self.stk.append(res.right)
                    while (self.stk[-1].left != None): self.stk.append(self.stk[-1].left)
        return res

class Solution:
    def countPairs (self, root1, root2, x):
        itr1, itr2 = BinaryTreeInOrderIterator(root1), BinaryTreeInOrderIterator(root2, True)
        ptr1, ptr2, res = itr1.getNext(), itr2.getNext(), 0
        while ((ptr1 != None) and (ptr2 != None)):
            sum = ptr1.data + ptr2.data
            if (sum == x): res, ptr1, ptr2 = res + 1, itr1.getNext(), itr2.getNext()
            elif (sum < x): ptr1 = itr1.getNext()
            else: ptr2 = itr2.getNext()
        return res
