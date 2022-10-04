def __graphColoringHelper (curr_node, graph, m, n, nodes_color_arr):
    for color in range(m):
        color_found_in_adj_nodes = False
        for adj_node in range(n):
            if ((graph[curr_node][adj_node] == 1) and (nodes_color_arr[adj_node] == color)):
                color_found_in_adj_nodes = False ; break
        if (not color_found_in_adj_nodes):
            nodes_color_arr[curr_node] = color
            if ((curr_node + 1) == n): return True
            if (__graphColoringHelper(curr_node + 1, graph, m, n, nodes_color_arr)): return True
            nodes_color_arr[curr_node] = -1
    return False

def graphColoring (graph, m, n):
    nodes_color_arr = [-1 for i in range(n)]
    return __graphColoringHelper(0, graph, m, n, nodes_color_arr)
