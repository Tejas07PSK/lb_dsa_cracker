from collections import deque
class Solution:
    def __isCyclicHelper (self, idx, prev_idx, adj_lst):
        self.visited[idx] = True ; self.curr_dfs_trace.add(idx)
        for vert in adj_lst[idx]:
            if (not self.visited[vert]):
                res = self.__isCyclicHelper(vert, idx, adj_lst)
                if (res): return True
            else:
                if (vert == idx): return True
                if ((vert in self.curr_dfs_trace) and (vert != prev_idx)): return True
        return False

    def isCycle (self, V, adj_lst):
        self.visited = [False for i in range(V)]
        for i in range(V):
            if (not self.visited[i]):
                self.curr_dfs_trace = set()
                res = self.__isCyclicHelper(i, None, adj_lst)
                if (res == True): return True
        return False
