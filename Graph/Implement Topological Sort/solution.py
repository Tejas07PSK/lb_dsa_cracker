from collections import deque

class Solution:
    def topoSort (self, V, adj):
        in_deg_arr, res = [0 for i in range(V)], []
        q = deque()
        for i in range(V):
            for vert in adj[i]: in_deg_arr[vert] += 1
        for i in range(V):
            if (in_deg_arr[i] == 0): q.append(i)
        while (q):
            curr_vert = q.popleft() ; res.append(curr_vert)
            for vert in adj[curr_vert]:
                in_deg_arr[vert] -= 1
                if (in_deg_arr[vert] == 0): q.append(vert)
        return res if (len(res) == V) else []
