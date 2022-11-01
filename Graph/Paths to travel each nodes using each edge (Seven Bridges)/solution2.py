from collections import deque
class Solution:
    def __findPath (self, curr_node, v):
        if (self.deg[curr_node] > 0):
            next_node = 0
            while (next_node < v):
                if (self.adj_lst[curr_node][next_node] == 1):
                    self.edges_covered += 1
                    self.deg[curr_node] -= 1 ; self.deg[next_node] -= 1
                    self.adj_lst[curr_node][next_node] = 0
                    self.adj_lst[next_node][curr_node] = 0
                    self.__findPath(next_node, v)
                next_node += 1
        self.path.appendleft(curr_node)

    def findEulerPathOrCircuit (self, v, e, edges):
        self.adj_lst = [[0 for j in range(v)] for i in range(v)]
        self.deg = [0 for i in range(v)]
        for start, end in edges:
            self.deg[start] += 1 ; self.deg[end] += 1
            self.adj_lst[start][end] = 1 ; self.adj_lst[end][start] = 1
        start_node, od_dg_cnt = None, 0
        for i in range(v):
            if ((self.deg[i] % 2) != 0):
                od_dg_cnt += 1
                if ((od_dg_cnt) > 2): return []
                if (start_node == None): start_node = i
        if (start_node == None): start_node = 0
        self.path, self.edges_covered = deque(), 0
        self.__findPath(start_node, v)
        return list(self.path) if (self.edges_covered == e) else []
