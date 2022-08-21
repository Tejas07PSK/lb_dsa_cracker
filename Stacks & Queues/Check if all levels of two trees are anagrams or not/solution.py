from typing import Optional
from collections import deque, defaultdict
"""
definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def areAnagrams (self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        if ((node1 == None) or (node2 == None)): return 0
        default_f = lambda : 0
        q1, q2 = deque(), deque()
        q1.append(node1) ; q2.append(node2)
        while ((q1) and (q2)):
            l1, l2 = len(q1), len(q2)
            hm1, hm2 = defaultdict(default_f), defaultdict(default_f)
            i, j = 0, 0
            while (i < l1):
                tmp_node_1 = q1.popleft()
                hm1[tmp_node_1.data] += 1
                if (tmp_node_1.left != None): q1.append(tmp_node_1.left)
                if (tmp_node_1.right != None): q1.append(tmp_node_1.right)
                i += 1
            while (j < l2):
                tmp_node_2 = q2.popleft()
                hm2[tmp_node_2.data] += 1
                if (tmp_node_2.left != None): q2.append(tmp_node_2.left)
                if (tmp_node_2.right != None): q2.append(tmp_node_2.right)
                j += 1
            if (len(hm1) != len(hm2)): return 0
            for key, value in hm2.items():
                if (hm1[key] != value): return 0
            del hm1, hm2
        if ((q1) or (q2)): return 0
        return 1
