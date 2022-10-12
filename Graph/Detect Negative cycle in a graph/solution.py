from math import inf
class Solution:
    def isNegativeWeightCycle (self, n, edges):
        if (len(edges) == 0): return 0
        change_obs, nd_dist_arr = False, [inf for i in range(n)]
        nd_dist_arr[edges[0][0]] = 0
        for i in range(n):
            change_obs = False
            for start, end, wt in edges:
                if ((nd_dist_arr[start] + wt) < nd_dist_arr[end]):
                    nd_dist_arr[end] = nd_dist_arr[start] + wt
                    change_obs = True
        return int(change_obs)
