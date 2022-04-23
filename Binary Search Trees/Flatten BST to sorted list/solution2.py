# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def flatten (self, root: Optional[TreeNode]) -> None:
        ptr = root
        while (ptr != None):
            if (ptr.left == None): ptr = ptr.right
            else:
                temp = ptr.left
                while (temp.right != None and temp.right != ptr): temp = temp.right
                if (temp.right == None): temp.right, ptr = ptr, ptr.left
                if (temp.right == ptr):
                    act_right = ptr.right
                    temp.right, ptr.right, ptr.left = ptr.right, ptr.left, None
                    ptr = act_right
