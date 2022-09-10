from collections import deque

class Solution:
    def bfsOfGraph (self, V, adj):
        visited = [False for i in range(V)]
        q, res = deque(), []
        q.append(0) ; visited[0] = True
        while (q):
            curr_vert = q.popleft() ; res.append(curr_vert)
            for vert in adj[curr_vert]:
                if (not visited[vert]):
                    q.append(vert) ; visited[vert] = True
        return res
