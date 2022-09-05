from collections import deque

'''
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    def __inorderTraversal (self, root):
        if (root == None): return []
        stk, res = deque(), []
        stk.append(root)
        while (stk[-1].left != None): stk.append(stk[-1].left)
        while (stk):
            tmp_node = stk.pop()
            res.append(tmp_node.data)
            if (tmp_node.right != None):
                stk.append(tmp_node.right)
                while (stk[-1].left != None): stk.append(stk[-1].left)
        return res

    def convertToMaxHeapUtil(self, root):
        if (root == None): return
        in_ord_trav_lst = self.__inorderTraversal(root)
        dq, i = deque(), -1
        dq.appendleft(root)
        while (dq):
            tmp_node = dq.popleft()
            tmp_node.data = in_ord_trav_lst[i] ; i -= 1
            if (tmp_node.left != None): dq.appendleft(tmp_node.left)
            if (tmp_node.right != None): dq.appendleft(tmp_node.right)
