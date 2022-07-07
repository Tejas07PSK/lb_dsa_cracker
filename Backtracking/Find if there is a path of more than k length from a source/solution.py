class Solution:
    def __pathMoreThanKHelper (self, root, path, graph, v, k):
        self.visited.add(root)
        for child in range(v):
            if ((child not in self.visited) and (graph[root][child] != None)):
                if ((path + graph[root][child]) >= k): return 1
                if (self.__pathMoreThanKHelper(child, (path + graph[root][child]), graph, v, k) == 1): return 1
        self.visited.discard(root)
        return 0

    def pathMoreThanK (self, v, e, k, a):
        graph, self.visited = [[None for i in range(v)] for j in range(v)], set()
        for i in range(0, len(a), 3):
            graph[a[i]][a[i+1]] = a[i+2]
            graph[a[i+1]][a[i]] = a[i+2]
        return self.__pathMoreThanKHelper(0, 0, graph, v, k)
