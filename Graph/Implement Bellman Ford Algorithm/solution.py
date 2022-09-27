from math import inf
class Solution:
    def isNegativeWeightCycle (self, n, edges):
        if (len(edges) == 0): return 0
        dists = [inf for i in range(n)]
        change_in_dists_observed = False
        dists[edges[0][0]] = 0
        for i in range(n):
            change_in_dists_observed = False
            for start, end, weight in edges:
                if (dists[start] + weight < dists[end]):
                    change_in_dists_observed = True
                    dists[end] = dists[start] + weight
        return int(change_in_dists_observed)
