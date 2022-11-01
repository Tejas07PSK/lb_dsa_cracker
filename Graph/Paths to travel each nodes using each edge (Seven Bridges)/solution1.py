from collections import deque
class Solution:
    def __findPath (self, curr_node):
        while (self.adj_lst[curr_node]):
            self.edges_covered += 1
            self.__findPath(self.adj_lst[curr_node].popleft())
        self.path.appendleft(curr_node)

    def findEulerPathOrCircuit (self, v, e, edges):
        self.adj_lst = [deque() for i in range(v)]
        in_deg, out_deg = [0 for i in range(v)], [0 for i in range(v)]
        for start, end in edges:
            out_deg[start] += 1 ; in_deg[end] += 1
            self.adj_lst[start].append(end)
        start_node, end_node = None, None
        for i in range(v):
            if (abs(in_deg[i] - out_deg[i]) > 1): return []
            elif ((in_deg[i] - out_deg[i]) == 1):
                if (end_node != None): return []
                end_node = i
            elif ((out_deg[i] - in_deg[i]) == 1):
                if (start_node != None): return []
                start_node = i
        if (start_node == None): start_node = 0
        self.path, self.edges_covered = deque(), 0
        self.__findPath(start_node)
        return list(self.path) if (self.edges_covered == e) else []
