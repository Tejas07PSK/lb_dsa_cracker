class Solution:
    def __isCyclicHelper (self, idx, adj_lst):
        self.visited[idx] = True
        self.curr_dfs_trace.add(idx)
        for vert in adj_lst[idx]:
            if (not self.visited[vert]):
                res = self.__isCyclicHelper (vert, adj_lst)
                if (res): return True
            elif (vert in self.curr_dfs_trace): return True
        self.curr_dfs_trace.remove(idx)
        return False

    def isCyclic (self, V, adj_lst):
        self.visited = [False for i in range(V)]
        self.curr_dfs_trace = set()
        for i in range(V):
            if (not self.visited[i]):
                res = self.__isCyclicHelper(i, adj_lst)
                if (res): return True
        return False
