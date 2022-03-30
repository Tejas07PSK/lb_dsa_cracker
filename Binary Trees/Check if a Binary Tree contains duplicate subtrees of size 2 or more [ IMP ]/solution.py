'''
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def __dupSubHelper (self, root):
        if (root == None): return [], False
        if ((root.left == None) and (root.right == None)): return [str(root.data)], False
        left_lst, right_lst = [], []
        left_state, right_state = False, False
        tmp_str = ''
        if (root.left != None):
            left_lst, left_state = self.__dupSubHelper(root.left)
            if (left_state): return left_lst, left_state
        if (root.right != None):
            right_lst, right_state = self.__dupSubHelper(root.right)
            if (right_state): return right_lst, right_state
        left_lst.append(str(root.data)) ; left_lst.extend(right_lst) ; tmp_str = ''.join(left_lst)
        if (tmp_str in self.seen_before): return left_lst, True
        self.seen_before.add(tmp_str)
        return left_lst, False

    def dupSub (self, root):
        self.seen_before = set()
        return 1 if self.__dupSubHelper(root)[1] else 0
