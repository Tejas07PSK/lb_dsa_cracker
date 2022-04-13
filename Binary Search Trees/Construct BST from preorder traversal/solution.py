# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def bstFromPreorder (self, preorder: List[int]) -> Optional[TreeNode]:
        stk = deque() ; stk.append(TreeNode(preorder[0])) ; root = stk[-1]
        for i in range(1, len(preorder)):
            if (preorder[i] < stk[-1].val):
                stk[-1].left = TreeNode(preorder[i]) ; stk.append(stk[-1].left)
            else:
                prev = stk.pop()
                while ((stk) and (preorder[i] > stk[-1].val)): prev = stk.pop()
                prev.right = TreeNode(preorder[i]) ; stk.append(prev.right)
        return root
