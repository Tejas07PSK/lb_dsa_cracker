from collections import deque
class Solution:
    def isCyclic (self, V, adj_lst):
        in_deg_arr, q, count = [0 for i in range(V)], deque(), 0
        for i in range(V):
            for vert in adj_lst[i]: in_deg_arr[vert] += 1
        for i in range(V):
            if (in_deg_arr[i] == 0): q.append(i)
        while (q):
            idx = q.popleft()
            count += 1
            for vert in adj_lst[idx]:
                in_deg_arr[vert] -= 1
                if (in_deg_arr[vert] == 0): q.append(vert)
        return True if (count != V) else False
