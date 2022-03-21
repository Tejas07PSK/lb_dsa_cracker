# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import deque
class Solution:
    def topView (self, root):
        if (root == None): return []
        res, q, v_lvl_hm = deque(), deque(), {}
        mx_vl_mn_vl = [0 , 0] ; q.append((root, 0))
        while (q):
            tree_node, curr_vl = q.popleft()
            if (curr_vl > mx_vl_mn_vl[0]): mx_vl_mn_vl[0] = curr_vl
            elif (curr_vl < mx_vl_mn_vl[1]): mx_vl_mn_vl[1] = curr_vl
            if (curr_vl not in v_lvl_hm): v_lvl_hm[curr_vl] = tree_node.data
            if (tree_node.left != None): q.append((tree_node.left, (curr_vl - 1)))
            if (tree_node.right != None): q.append((tree_node.right, (curr_vl + 1)))
        return [v_lvl_hm[i] for i in range(mx_vl_mn_vl[1], mx_vl_mn_vl[0] + 1)]
