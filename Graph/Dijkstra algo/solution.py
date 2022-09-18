from math import inf
class Solution:
    def dijkstra (self, v, adj_lst, s):
        tmp_hm = [inf for i in range(v)] ; tmp_hm[s] = 0
        visited, count = set(), 0
        min_val, min_idx = 0, s
        while (count < v):
            visited.add(min_idx)
            for adj_idx in adj_lst[min_idx]:
                if (adj_idx[0] not in visited):
                    if ((tmp_hm[min_idx] + adj_idx[1]) < tmp_hm[adj_idx[0]]):
                        tmp_hm[adj_idx[0]] = tmp_hm[min_idx] + adj_idx[1]
            min_val, min_idx = inf, -1
            for i in range(len(tmp_hm)):
                if (i not in visited):
                    if (tmp_hm[i] < min_val): min_val, min_idx = tmp_hm[i], i
            count += 1
        return tmp_hm
