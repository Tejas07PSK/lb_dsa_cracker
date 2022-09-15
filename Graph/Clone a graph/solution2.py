from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph (self, node: 'Node') -> 'Node':
        if (node == None): return None
        q, visited_hm = deque(), {}
        q.append((node, Node(node.val, []))) ; visited_hm[node] = q[0][1]
        while (q):
            curr_node, curr_node_clone = q.popleft()
            for next_node in curr_node.neighbors:
                if (next_node not in visited_hm):
                    visited_hm[next_node] = Node(next_node.val, [])
                    q.append((next_node, visited_hm[next_node]))
                curr_node_clone.neighbors.append(visited_hm[next_node])
        return visited_hm[node]
