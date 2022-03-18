# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__ (self):
        self.res = []

    def inorderTraversal (self, root: Optional[TreeNode]) -> List[int]:
        if (root == None): return self.res
        if (root.left != None): self.inorderTraversal(root.left)
        self.res.append(root.val)
        if (root.right != None): self.inorderTraversal(root.right)
        return self.res
