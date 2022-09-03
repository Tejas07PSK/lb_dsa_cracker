from collections import deque
'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def isHeap (self, root):
        if (root == None): return True
        q = deque() ; q.append(root)
        next_lvl_has_any_ele = True
        while (next_lvl_has_any_ele):
            next_lvl_has_any_ele = False
            curr_no_of_eles = len(q)
            i = 0
            while (i < curr_no_of_eles):
                curr_ele, i = q.popleft(), i + 1
                if ((curr_ele == None) and (q) and (q[0] != None)): return False
                if (curr_ele != None):
                    if (curr_ele.left != None):
                        if (curr_ele.data < curr_ele.left.data): return False
                        next_lvl_has_any_ele = True
                    q.append(curr_ele.left)
                    if (curr_ele.right != None):
                        if (curr_ele.data < curr_ele.right.data): return False
                        next_lvl_has_any_ele = True
                    q.append(curr_ele.right)
        return True
