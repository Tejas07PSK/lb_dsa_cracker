from collections import deque

'''
----Binary tree node class for reference-----
class BinaryTreeNode:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
'''

def inorderTraversal (root):
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

def convertBST (root):
    if (root == None): return root
    in_ord_trav_items = inorderTraversal(root)
    dq, i = deque(), 0
    dq.appendleft(root)
    while (dq):
        tmp_node = dq.popleft()
        tmp_node.data = in_ord_trav_items[i] ; i += 1
        if (tmp_node.right != None): dq.appendleft(tmp_node.right)
        if (tmp_node.left != None): dq.appendleft(tmp_node.left)
    return root
