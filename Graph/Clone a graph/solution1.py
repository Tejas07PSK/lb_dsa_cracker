"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __dfs_helper (self, curr_node, curr_node_clone):
        for next_node in curr_node.neighbors:
            if (next_node not in self.visited_hm):
                self.visited_hm[next_node] = Node(next_node.val, [])
                self.__dfs_helper(next_node, self.visited_hm[next_node])
            curr_node_clone.neighbors.append(self.visited_hm[next_node])

    def cloneGraph (self, node: 'Node') -> 'Node':
        if (node == None): return None
        self.visited_hm = {}
        self.visited_hm[node] = Node(node.val, [])
        self.__dfs_helper(node, self.visited_hm[node])
        return self.visited_hm[node]
