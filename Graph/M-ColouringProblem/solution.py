def __graphColoringHelper (curr_node, col_arr, k, v):
    for color in range(k):
        col_found_in_adj_nodes = False
        for adj_node in range(v):
            if ((graph[curr_node][adj_node] == 1) and (col_arr[adj_node] == color)):
                col_found_in_adj_nodes = True ; break
        if (not col_found_in_adj_nodes):
            col_arr[curr_node] = color
            if ((curr_node + 1) == v): return 1
            if (__graphColoringHelper(curr_node + 1, col_arr, k, v) == 1): return 1
            col_arr[curr_node] = -1
    return 0

def graphColoring (graph, k, V):
    col_arr = [-1 for i in range(V)]
    return (__graphColoringHelper(0, col_arr, k, V))
