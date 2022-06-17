class Solution:
    def __graphColoringHelper (self, node, graph, n, m):
        for color in range(1, m + 1):
            color_found_in_adj_nodes = False
            for adj_node in range(n):
                if ((graph[node][adj_node] == 1) and (self.nodes_color[adj_node] == color)):
                    color_found_in_adj_nodes = True ; break
            if (not color_found_in_adj_nodes):
                self.nodes_color[node] = color
                if ((node + 1) == n): return True
                if (self.__graphColoringHelper(node + 1, graph, n, m)): return True
                self.nodes_color[node] = 0
        return False

    def graphColoring (self, graph, m, n):
        self.nodes_color = [0 for i in range(n)]
        return self.__graphColoringHelper(0, graph, n, m)

def graphColoring (graph, m, n):
    return Solution().graphColoring(graph, m, n)
