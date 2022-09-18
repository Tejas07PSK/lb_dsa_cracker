from math import inf
class Solution:
    def dijkstra (self, v, adj_lst, s):
        tmp_hm = [inf for i in range(v)] ; tmp_hm[s] = 0
        visited, count = set(), 0
        min_val, min_idx = inf, s
        while (count < v):
            curr_idx = min_idx
            min_val, min_idx = inf, -1
            for adj_idx in adj_lst[curr_idx]:
                if (adj_idx[0] not in visited):
                    if ((tmp_hm[curr_idx] + adj_idx[1]) < tmp_hm[adj_idx[0]]):
                        tmp_hm[adj_idx[0]] = tmp_hm[curr_idx] + adj_idx[1]
                    if (tmp_hm[adj_idx[0]] < min_val):
                        min_val = tmp_hm[adj_idx[0]] ; min_idx = adj_idx[0]
            count += 1
        return tmp_hm
