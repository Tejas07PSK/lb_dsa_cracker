from collections import deque
class Solution:
    def isPossible (self, N, prerequisites):
        count, in_deg_arr, adj_lst, q = 0, [0 for i in range(N)], [[] for i in range(N)], deque()
        for start, end in prerequisites:
            in_deg_arr[end] += 1 ; adj_lst[start].append(end)
        for i in range(N):
            if (in_deg_arr[i] == 0): q.append(i)
        while (q):
            count += 1
            curr_vert = q.popleft()
            for next_vert in adj_lst[curr_vert]:
                in_deg_arr[next_vert] -= 1
                if (in_deg_arr[next_vert] == 0): q.append(next_vert)
        return True if (count == N) else False
