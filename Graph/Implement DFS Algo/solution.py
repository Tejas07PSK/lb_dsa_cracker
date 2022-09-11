class Solution:
    def __dfs_helper (self, idx, adj):
        self.res.append(idx)
        self.visited[idx] = True
        for vert in adj[idx]:
            if (not self.visited[vert]): self.__dfs_helper(vert, adj)

    def dfsOfGraph (self, V, adj):
        self.visited, self.res = [False for i in range(V)], []
        self.__dfs_helper(0, adj)
        return self.res
