# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    def __constructMinHeightBST (self, l, r):
        if (l == r): return Node(self.in_ord_arr[l])
        mid = l + ((r - l) // 2) ; root = Node(self.in_ord_arr[mid])
        if ((mid - 1) >= l): root.left = self.__constructMinHeightBST(l, (mid - 1))
        if ((mid + 1) <= r): root.right = self.__constructMinHeightBST((mid + 1), r)
        return root

    def __inOrderHelper (self, root):
        if (root.left != None): self.__inOrderHelper(root.left)
        self.in_ord_arr.append(root.data)
        if (root.right != None): self.__inOrderHelper(root.right)

    def buildBalancedTree (self, root):
        if (root == None): return root
        self.in_ord_arr = [] ; self.__inOrderHelper(root)
        return self.__constructMinHeightBST(0, len(self.in_ord_arr) - 1)
