# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def preorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        if (root == None): return []
        res, stk = [], deque() ; stk.append(root) ; res.append(root.val)
        while (stk):
            while (root.left != None):
                root = root.left ; stk.append(root) ; res.append(root.val)
            if (root.right == None):
                root = stk.pop()
                while (stk):
                    if ((stk[-1].right == root) or (stk[-1].right == None)): root = stk.pop()
                    else:
                        root = stk[-1].right ; stk.append(root); res.append(root.val) ; break
            else:
                root = root.right ; stk.append(root) ; res.append(root.val)
        return res
