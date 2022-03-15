from collections import deque
class Solution:
    def levelOrder (self, root):
        if (root == None): return []
        res, q = [], deque()
        q.append(root)
        while (q):
            tree_node = q.popleft()
            res.append(tree_node.data)
            if (tree_node.left != None): q.append(tree_node.left)
            if (tree_node.right != None): q.append(tree_node.right)
        return res
