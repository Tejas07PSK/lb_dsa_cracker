# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    def __inOrderHelper (self, root, l, h):
        if (root == None): return
        if (root.left != None): self.__inOrderHelper(root.left, l, h)
        if (l <= root.data <= h): self.count += 1
        if (root.right != None): self.__inOrderHelper(root.right, l, h)

    def getCountOfNode (self, root, l, h):
        self.count = 0 ; self.__inOrderHelper(root, l, h)
        return self.count

def getCount(root,low,high):
    return Solution().getCountOfNode(root, low, high)
