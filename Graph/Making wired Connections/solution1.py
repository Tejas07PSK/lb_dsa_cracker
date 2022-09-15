class Solution:
    def __dfs_helper (self, curr_vert, adj_lst):
        for vert in adj_lst[curr_vert]:
            if (not self.visited[vert]):
                self.visited[vert] = True
                self.__dfs_helper(vert, adj_lst)

    def makeConnected (self, n: int, connections: List[List[int]]) -> int:
        if (len(connections) < (n - 1)): return -1
        adj_lst = [[] for i in range(n)]
        for start, end in connections:
            adj_lst[start].append(end) ; adj_lst[end].append(start)
        self.visited, conn_comps = [False for i in range(n)], 0
        for i in range(n):
            if (not self.visited[i]):
                conn_comps += 1
                self.visited[i] = True
                self.__dfs_helper(i, adj_lst)
        return conn_comps - 1
