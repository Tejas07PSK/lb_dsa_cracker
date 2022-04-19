class Node:
    def __init__ (self, data): self.data, self.height, self.left, self.right = data, 0, None, None

class AVLTree:
    def __init__ (self):
        self.root = None
        self.height_calc_util = lambda n: n.height if (n != None) else 0
        self.curr_in_ord_succ = -1

    def __insertHelper (self, root, val):
        if (root == None): return Node(val)
        if (val < root.data):
            self.curr_in_ord_succ = root.data
            if (root.left == None): root.left = Node(val)
            else: root.left = self.__insertHelper(root.left, val)
        else:
            if (root.right == None): root.right = Node(val)
            else: root.right = self.__insertHelper(root.right, val)
        root.height = max(self.height_calc_util(root.left), self.height_calc_util(root.right)) + 1
        bf = abs(self.height_calc_util(root.left) - self.height_calc_util(root.right))
        if (bf > 1):
            tmp_root = None
            r_l_h, r_r_h = self.height_calc_util(root.left), self.height_calc_util(root.right)
            if (r_l_h > r_r_h):
                r_l_l_h, r_l_r_h = self.height_calc_util(root.left.left), self.height_calc_util(root.left.right)
                if (r_l_l_h > r_l_r_h):
                    tmp_root = root.left ; self.__LLrotate(root, root.left) ; root = tmp_root
                else:
                    tmp_root = root.left.right ; self.__LRrotate(root, root.left, root.left.right) ; root = tmp_root
            else:
                r_r_l_h, r_r_r_h = self.height_calc_util(root.right.left), self.height_calc_util(root.right.right)
                if (r_r_l_h > r_r_r_h):
                    tmp_root = root.right.left ; self.__RLrotate(root, root.right, root.right.left) ; root = tmp_root
                else:
                    tmp_root = root.right ; self.__RRrotate(root, root.right) ; root = tmp_root
        return root

    def insertIntoAvl (self, val):
        self.curr_in_ord_succ = -1 ; self.root = self.__insertHelper(self.root, val)

    def __LLrotate (self, node1, node2):
        node1.left, node2.right = node2.right, node1
        node1.height = max(self.height_calc_util(node1.left), self.height_calc_util(node1.right)) + 1
        node2.height = max(self.height_calc_util(node2.left), self.height_calc_util(node2.right)) + 1
    
    def __RRrotate (self, node1, node2):
        node1.right, node2.left = node2.left, node1
        node1.height = max(self.height_calc_util(node1.left), self.height_calc_util(node1.right)) + 1
        node2.height = max(self.height_calc_util(node2.left), self.height_calc_util(node2.right)) + 1
    
    def __LRrotate (self, node1, node2, node3):
        node1.left, node2.right, node3.right, node3.left = node3.right, node3.left, node1, node2
        node1.height = max(self.height_calc_util(node1.left), self.height_calc_util(node1.right)) + 1
        node2.height = max(self.height_calc_util(node2.left), self.height_calc_util(node2.right)) + 1
        node3.height = max(self.height_calc_util(node3.left), self.height_calc_util(node3.right)) + 1
    
    def __RLrotate (self, node1, node2, node3):
        node2.left, node1.right, node3.right, node3.left = node3.right, node3.left, node2, node1
        node1.height = max(self.height_calc_util(node1.left), self.height_calc_util(node1.right)) + 1
        node2.height = max(self.height_calc_util(node2.left), self.height_calc_util(node2.right)) + 1
        node3.height = max(self.height_calc_util(node3.left), self.height_calc_util(node3.right)) + 1

def leastGreaterElement (arr):
    tree = AVLTree()
    for i in range(len(arr) - 1, -1, -1):
        tree.insertIntoAvl(arr[i]) ; arr[i] = tree.curr_in_ord_succ
    return arr
