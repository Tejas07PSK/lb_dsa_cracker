def spanningTrees (adjMatrix, n, m):
    edges, is_complete = 0, True
    for i in range(n):
        for j in range(n):
            if (i != j):
                if (adjMatrix[i][j] == 1):
                    adjMatrix[j][j] += 1
                    adjMatrix[i][j] = -1
                    if (adjMatrix[j][i] != -1): edges += 1
                else: is_complete = False
    if (edges == (n - 1)): return 1
    if (is_complete == True): return (n ** (n - 2))
    factor, det = 1, 1
    for i in range(1, n):
        if (adjMatrix[i][i] == 0): return 0
        det *= adjMatrix[i][i]
        for j in range(i + 1, n):
            if (adjMatrix[j][i] != 0):
                factor *= adjMatrix[i][i]
                temp = adjMatrix[j][i]
                for k in range(i, n):
                    adjMatrix[j][k] = ((adjMatrix[i][i] * adjMatrix[j][k]) - (temp * adjMatrix[i][k]))
    return abs(det // factor)
