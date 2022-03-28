# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def buildTree (self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pre_order_len, in_order_len = len(preorder), len(inorder)
        if ((not pre_order_len) or (not in_order_len)): return None
        p, i, stk, to_right = 0, 0, deque(), False
        ptr = root = TreeNode(preorder[p]); stk.append(root) ; p += 1
        while (p < pre_order_len):
            if ((i < in_order_len) and (stk) and (stk[-1].val == inorder[i])):
                while ((i < in_order_len) and (stk) and (stk[-1].val == inorder[i])):
                    ptr = stk.pop() ; i += 1
                to_right = True
            if (to_right):
                ptr.right = TreeNode(preorder[p]) ; ptr = ptr.right
                stk.append(ptr) ; to_right = False
            else:
                ptr.left = TreeNode(preorder[p]) ; ptr = ptr.left
                stk.append(ptr)
            p += 1
        return root
