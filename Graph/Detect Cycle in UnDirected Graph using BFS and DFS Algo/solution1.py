class Solution:
    def __isCyclicHelper (self, idx, prev_idx, adj_lst):
        self.visited[idx] = True
        for vert in adj_lst[idx]:
            if (not self.visited[vert]):
                res = self.__isCyclicHelper(vert, idx, adj_lst)
                if (res): return True
            else:
                if (vert == idx): return True
                if (vert != prev_idx): return True
        return False

    def isCycle (self, V, adj_lst):
        self.visited = [False for i in range(V)]
        for i in range(V):
            if (not self.visited[i]):
                res = self.__isCyclicHelper(i, None, adj_lst)
                if (res == True): return True
        return False
