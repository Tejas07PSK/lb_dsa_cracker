# Definition for a binary tree node.
# class TreeNode:
#     def __init__ (self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode (self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if (root == None): return root
        prev, ptr = None, root
        while (ptr != None):
            if (key == ptr.val):
                node = None
                if ((ptr.left != None) and (ptr.right == None)): node = ptr.left
                elif ((ptr.left == None) and (ptr.right != None)): node = ptr.right
                elif ((ptr.left != None) and (ptr.right != None)):
                    node = ptr.right
                    if (node.left != None):
                        tmp_prev = node ; node = node.left
                        while (node.left != None): tmp_prev, node = node, node.left
                        tmp_prev.left = node.right ; node.right = ptr.right
                    node.left = ptr.left
                if (prev != None):
                    if (prev.left == ptr): prev.left = node
                    else: prev.right = node
                else: root = node
                ptr.left, ptr.right = None, None
                break
            elif (key < ptr.val): prev, ptr = ptr, ptr.left
            else: prev, ptr = ptr, ptr.right
        return root
