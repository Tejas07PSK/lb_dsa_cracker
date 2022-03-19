# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.res = []

    def preorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        if (root == None): return self.res
        self.res.append(root.val)
        if (root.left != None): self.preorderTraversal(root.left)
        if (root.right != None): self.preorderTraversal(root.right)
        return self.res
