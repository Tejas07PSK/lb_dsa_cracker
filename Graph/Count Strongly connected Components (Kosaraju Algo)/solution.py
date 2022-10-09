from collections import deque
class Solution:
    def __dfs_helper (self, curr_node, graph, is_prep_stage):
        for next_node in graph[curr_node]:
            if (not self.visited[next_node]):
                self.visited[next_node] = True
                self.__dfs_helper(next_node, graph, is_prep_stage)
            if (is_prep_stage): self.t_graph[next_node].append(curr_node)
        if (is_prep_stage): self.aux_stk.append(curr_node)

    def kosaraju (self, v, adj_lst):
        self.visited = [False for i in range(v)]
        self.t_graph = [deque() for i in range(v)]
        self.aux_stk = deque()
        self.scc_count = 0
        for i in range(v):
            if (not self.visited[i]):
                self.visited[i] = True
                self.__dfs_helper(i, adj_lst, True)
        del self.visited ; self.visited = [False for i in range(v)]
        while (self.aux_stk):
            i = self.aux_stk.pop()
            if (not self.visited[i]):
                self.visited[i] = True
                self.__dfs_helper(i, self.t_graph, False)
                self.scc_count += 1
        return self.scc_count
