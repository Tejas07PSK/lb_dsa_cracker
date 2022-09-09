def printAdjacency (n, m, edges):
    adj_lists = [[] for i in range(n)]
    for start, end in edges:
        adj_lists[start].append(end)
        adj_lists[end].append(start)
    for i in range(n):
        adj_lists[i].append(i)
        adj_lists[i].reverse()
    return adj_lists
