class TreeNode:
    def __init__ (self, val):
        self.val = val
        self.freq = 1
        self.children = 0
        self.height = 0
        self.left = None
        self.right = None

class Solution:
    def __LL_rotate (self, node_1, node_2):
        node_1.left = node_2.right
        node_2.right = node_1
        height_left = node_1.left.height if (node_1.left != None) else 0
        height_right = node_1.right.height if (node_1.right != None) else 0
        node_1.height = 1 + max(height_left, height_right)
        right_cntr = (node_1.right.children + node_1.right.freq) if (node_1.right != None) else 0
        left_cntr = (node_1.left.children + node_1.left.freq) if (node_1.left != None) else 0
        node_1.children = right_cntr + left_cntr
        height_left = node_2.left.height if (node_2.left != None) else 0
        height_right = node_2.right.height if (node_2.right != None) else 0
        node_2.height = 1 + max(height_left, height_right)
        right_cntr = (node_2.right.children + node_2.right.freq) if (node_2.right != None) else 0
        left_cntr = (node_2.left.children + node_2.left.freq) if (node_2.left != None) else 0
        node_2.children = right_cntr + left_cntr
        return node_2

    def __RR_rotate (self, node_1, node_2):
        node_1.right = node_2.left
        node_2.left = node_1
        height_left = node_1.left.height if (node_1.left != None) else 0
        height_right = node_1.right.height if (node_1.right != None) else 0
        node_1.height = 1 + max(height_left, height_right)
        right_cntr = (node_1.right.children + node_1.right.freq) if (node_1.right != None) else 0
        left_cntr = (node_1.left.children + node_1.left.freq) if (node_1.left != None) else 0
        node_1.children = right_cntr + left_cntr
        height_left = node_2.left.height if (node_2.left != None) else 0
        height_right = node_2.right.height if (node_2.right != None) else 0
        node_2.height = 1 + max(height_left, height_right)
        right_cntr = (node_2.right.children + node_2.right.freq) if (node_2.right != None) else 0
        left_cntr = (node_2.left.children + node_2.left.freq) if (node_2.left != None) else 0
        node_2.children = right_cntr + left_cntr
        return node_2

    def __LR_rotate (self, node_1, node_2, node_3):
        node_1.left = node_3.right
        node_2.right = node_3.left
        node_3.left = node_2
        node_3.right = node_1
        height_left = node_1.left.height if (node_1.left != None) else 0
        height_right = node_1.right.height if (node_1.right != None) else 0
        node_1.height = 1 + max(height_left, height_right)
        right_cntr = (node_1.right.children + node_1.right.freq) if (node_1.right != None) else 0
        left_cntr = (node_1.left.children + node_1.left.freq) if (node_1.left != None) else 0
        node_1.children = right_cntr + left_cntr
        height_left = node_2.left.height if (node_2.left != None) else 0
        height_right = node_2.right.height if (node_2.right != None) else 0
        node_2.height = 1 + max(height_left, height_right)
        right_cntr = (node_2.right.children + node_2.right.freq) if (node_2.right != None) else 0
        left_cntr = (node_2.left.children + node_2.left.freq) if (node_2.left != None) else 0
        node_2.children = right_cntr + left_cntr
        height_left = node_3.left.height if (node_3.left != None) else 0
        height_right = node_3.right.height if (node_3.right != None) else 0
        node_3.height = 1 + max(height_left, height_right)
        right_cntr = (node_3.right.children + node_3.right.freq) if (node_3.right != None) else 0
        left_cntr = (node_3.left.children + node_3.left.freq) if (node_3.left != None) else 0
        node_3.children = right_cntr + left_cntr
        return node_3

    def __RL_rotate (self, node_1, node_2, node_3):
        node_1.right = node_3.left
        node_2.left = node_3.right
        node_3.right = node_2
        node_3.left = node_1
        height_left = node_1.left.height if (node_1.left != None) else 0
        height_right = node_1.right.height if (node_1.right != None) else 0
        node_1.height = 1 + max(height_left, height_right)
        right_cntr = (node_1.right.children + node_1.right.freq) if (node_1.right != None) else 0
        left_cntr = (node_1.left.children + node_1.left.freq) if (node_1.left != None) else 0
        node_1.children = right_cntr + left_cntr
        height_left = node_2.left.height if (node_2.left != None) else 0
        height_right = node_2.right.height if (node_2.right != None) else 0
        node_2.height = 1 + max(height_left, height_right)
        right_cntr = (node_2.right.children + node_2.right.freq) if (node_2.right != None) else 0
        left_cntr = (node_2.left.children + node_2.left.freq) if (node_2.left != None) else 0
        node_2.children = right_cntr + left_cntr
        height_left = node_3.left.height if (node_3.left != None) else 0
        height_right = node_3.right.height if (node_3.right != None) else 0
        node_3.height = 1 + max(height_left, height_right)
        right_cntr = (node_3.right.children + node_3.right.freq) if (node_3.right != None) else 0
        left_cntr = (node_3.left.children + node_3.left.freq) if (node_3.left != None) else 0
        node_3.children = right_cntr + left_cntr
        return node_3

    def __avl_insert (self, root, val):
        if (root == None): return TreeNode(val)
        if (val < root.val):
            right_cntr = (root.right.children + root.right.freq) if (root.right != None) else 0
            self.inv_cntr += root.freq + right_cntr
            root.left = self.__avl_insert(root.left, val)
        elif (val > root.val): root.right = self.__avl_insert(root.right, val)
        else:
            root.freq += 1
            right_cntr = (root.right.children + root.right.freq) if (root.right != None) else 0
            self.inv_cntr += right_cntr
        height_left = root.left.height if (root.left != None) else 0
        height_right = root.right.height if (root.right != None) else 0
        root.height = 1 + max(height_left, height_right)
        right_cntr = (root.right.children + root.right.freq) if (root.right != None) else 0
        left_cntr = (root.left.children + root.left.freq) if (root.left != None) else 0
        root.children = right_cntr + left_cntr
        node_1 = root
        bf = height_left - height_right
        if (bf == 2):
            node_2 = node_1.left
            height_left = node_2.left.height if (node_2.left != None) else 0
            height_right = node_2.right.height if (node_2.right != None) else 0
            bf = height_left - height_right
            if (bf == 1):
                root = self.__LL_rotate(node_1, node_2)
            elif (bf == -1):
                node_3 = node_2.right
                root = self.__LR_rotate(node_1, node_2, node_3)
        elif (bf == -2):
            node_2 = node_1.right
            height_left = node_2.left.height if (node_2.left != None) else 0
            height_right = node_2.right.height if (node_2.right != None) else 0
            bf = height_left - height_right
            if (bf == 1):
                node_3 = node_2.left
                root = self.__RL_rotate(node_1, node_2, node_3)
            elif (bf == -1):
                root = self.__RR_rotate(node_1, node_2)
        return root

    def inversionCount (self, arr, n):
        self.inv_cntr = 0
        root = None
        for val in arr: root = self.__avl_insert(root, val)
        return self.inv_cntr
