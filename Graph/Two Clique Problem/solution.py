from collections import deque

def twoCliques (n: int, edgeList: list):
    color = [-1 for i in range(n)]
    adj_mat = [[1 if (i != j) else 0 for i in range(n)] for j in range(n)]
    for start, end in edgeList:
        adj_mat[start][end] = 0
        adj_mat[end][start] = 0
    stk = deque()
    for i in range(n):
        if (color[i] == -1):
            color[i] = 0
            stk.append((None, i))
            while (stk):
                parent_node, curr_node = stk.popleft()
                next_color = 1 if (color[curr_node] == 0) else 0
                for next_node in range(n):
                    if ((adj_mat[curr_node][next_node] == 1) and (next_node != parent_node)):
                        if (color[curr_node] == color[next_node]): return False
                        if (color[next_node] == -1):
                            color[next_node] = next_color
                            stk.append((curr_node, next_node))
    return True
