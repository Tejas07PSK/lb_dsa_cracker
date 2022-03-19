# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def inorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        if (root == None): return []
        res, stk = [], deque() ; stk.append(root)
        while (stk):
            while (root.left != None):
                stk.append(root.left) ; root = root.left
            res.append(root.val)
            if (root.right == None):
                root = stk.pop()
                while (stk):
                    if (stk[-1].right == root):
                        root = stk.pop()
                    else:
                        res.append(stk[-1].val)
                        if (stk[-1].right != None):
                            root = stk[-1].right ; stk.append(root) ; break
                        else: root = stk.pop()
            else:
                stk.append(root.right) ; root = root.right
        return res
