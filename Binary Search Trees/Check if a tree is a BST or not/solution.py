# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    def __isBSTHelper (self, root):
        if (root == None): return 0, 0, True
        ovr_left_state, ovr_right_state = True, True
        min_curr_tree, max_curr_tree = root.data, root.data
        if (root.left != None):
            min_from_left_tree, max_from_left_tree, left_is_bst = self.__isBSTHelper(root.left)
            if (not left_is_bst): return min_from_left_tree, max_from_left_tree, False
            ovr_left_state = (root.data > root.left.data) and (root.data > max_from_left_tree)
            min_curr_tree = min(min_curr_tree, min_from_left_tree)
            max_curr_tree = max(max_curr_tree, max_from_left_tree)
        if (root.right != None):
            min_from_right_tree, max_from_right_tree, right_is_bst = self.__isBSTHelper(root.right)
            if (not right_is_bst): return min_from_right_tree, max_from_right_tree, False
            ovr_right_state = (root.data < root.right.data) and (root.data < min_from_right_tree)
            min_curr_tree = min(min_curr_tree, min_from_right_tree)
            max_curr_tree = max(max_curr_tree, max_from_right_tree)
        return min_curr_tree, max_curr_tree, (ovr_left_state and ovr_right_state)

    def isBST (self, root):
        return self.__isBSTHelper(root)[2]
