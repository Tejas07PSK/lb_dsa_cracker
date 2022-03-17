# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree (self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if (root == None): return root
        q = deque() ; q.append(root)
        while (q):
            tree_node = q.popleft()
            if (tree_node.left != None): q.append(tree_node.left)
            if (tree_node.right != None): q.append(tree_node.right)
            tree_node.left, tree_node.right = tree_node.right, tree_node.left
        return root
