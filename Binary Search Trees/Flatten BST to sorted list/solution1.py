# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __flattenHelper (self, root):
        if (root == None): return None
        head, tail = root, root
        head_left, tail_left = None, None
        head_right, tail_right = None, None
        if (root.left != None): head_left, tail_left = self.__flattenHelper(root.left)
        if (root.right != None): head_right, tail_right = self.__flattenHelper(root.right)
        if ((head_left != None) and (head_right != None)):
            head.left = None ; tail_left.right = head_right
            head.right = head_left ; tail = tail_right
        elif ((head_left != None) and (head_right == None)):
            head.left = None ; head.right = head_left ; tail = tail_left
        elif ((head_left == None) and (head_right != None)):
            head.right = head_right ; tail = tail_right
        return head, tail
            
    def flatten (self, root: Optional[TreeNode]) -> None:
        self.__flattenHelper(root)
