from collections import deque
class Solution:
    def checkMirrorTree (self, n, e, A, B):
        node_children_map = {}
        for i in range(0, (2 * e), 2):
            if (A[i] not in node_children_map): node_children_map[A[i]] = deque()
            node_children_map[A[i]].append(A[i + 1])
        for j in range(0, (2 * e), 2):
            if ((B[j] not in node_children_map) or (not node_children_map[B[j]]) or (node_children_map[B[j]].pop() != B[j + 1])): return 0
        return 1
