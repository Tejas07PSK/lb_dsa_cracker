# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import deque
class Solution:
    def zigZagTraversal (self, root):
        if (root == None): return []
        res, q, q_size = deque(), deque(), 1
        should_reverse = False ; q.append(root)
        while (q):
            nxt_lvl_size = 0
            while (q_size > 0):
                tree_node = q.popleft() if (not should_reverse) else q.pop()
                res.append(tree_node.data) ; q_size -= 1
                if (not should_reverse):
                    if (tree_node.left != None):
                        nxt_lvl_size += 1 ; q.append(tree_node.left)
                    if (tree_node.right != None):
                        nxt_lvl_size += 1 ; q.append(tree_node.right)
                else:
                    if (tree_node.right != None):
                        nxt_lvl_size += 1 ; q.appendleft(tree_node.right)
                    if (tree_node.left != None):
                        nxt_lvl_size += 1 ; q.appendleft(tree_node.left)
            q_size, should_reverse = nxt_lvl_size, not should_reverse
        return res
