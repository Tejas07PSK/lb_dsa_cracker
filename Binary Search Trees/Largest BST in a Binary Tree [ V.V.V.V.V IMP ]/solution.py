from math import inf
class Solution:
    def __largestBSTHelper (self, root):
        if (root == None): return 0, inf, -inf
        curr_max, curr_min = root.data, root.data
        left_max, left_min = -inf, inf
        right_max, right_min = -inf, inf
        left_count, right_count = 0, 0
        left_val, right_val = -inf, inf
        left_state, right_state = True, True
        if (root.left != None):
            left_count, left_max, left_min, left_state = self.__largestBSTHelper(root.left)
            left_val = root.left.data
        if (root.right != None):
            right_count, right_max, right_min, right_state = self.__largestBSTHelper(root.right)
            right_val = root.right.data
        count = left_count + right_count + 1
        curr_state = False
        curr_max, curr_min = max(curr_max, left_max, right_max), min(curr_min, left_min, right_min)
        if (left_state and right_state and (root.data > left_val) and (root.data > left_max) and (root.data < right_val) and (root.data < right_min)):
            curr_state = True
            self.lg_bst = max(self.lg_bst, count)
        return count, curr_max, curr_min, curr_state

    def largestBst(self, root):
        self.lg_bst = 0 ; self.__largestBSTHelper(root)
        return self.lg_bst
