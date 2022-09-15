from collections import deque
class Solution:
    def makeConnected (self, n: int, connections: List[List[int]]) -> int:
        if (len(connections) < (n - 1)): return -1
        adj_lst = [[] for i in range(n)]
        for start, end in connections:
            adj_lst[start].append(end) ; adj_lst[end].append(start)
        q, visited, conn_comps = deque(), [False for i in range(n)], 0
        # apply bfs
        for i in range(n):
            if (not visited[i]):
                conn_comps += 1
                visited[i] = True
                q.append(i)
                while (q):
                    curr_vert = q.popleft()
                    for vert in adj_lst[curr_vert]:
                        if (not visited[vert]):
                            visited[vert] = True
                            q.append(vert)
        return conn_comps - 1
