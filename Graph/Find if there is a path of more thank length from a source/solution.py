class Solution:
    def __pathMoreThanKHelper (self, curr_node, path_sum, graph, k):
        self.visited.add(curr_node)
        for next_node, weight in graph[curr_node]:
            if (next_node not in self.visited):
                if ((path_sum + weight) >= k): return 1
                if (self.__pathMoreThanKHelper(next_node, (path_sum + weight), graph, k) == 1): return 1
        self.visited.discard(curr_node)
        return 0

    def pathMoreThanK (self, v, e, k, a):
        graph, self.visited = [[] for i in range(v)], set()
        for i in range(0, len(a) - 2, 3):
            graph[a[i]].append([a[i + 1], a[i + 2]])
            graph[a[i + 1]].append([a[i], a[i + 2]])
        return self.__pathMoreThanKHelper(0, 0, graph, k)
