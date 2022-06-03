from math import inf
class Solution:
    def k_centres_greedy (self, n, k, mat):
        centres, temp_dists, max_dist_idx = set(), [inf for i in range(n)], 0
        for i in range(k):
            centres.add(max_dist_idx)
            for j in range(n): temp_dists[j] = min(temp_dists[j], mat[max_dist_idx][j])
            for j in range(n):
                if ((j not in centres) and (temp_dists[j] > temp_dists[max_dist_idx])): max_dist_idx = j
        return temp_dists[max_dist_idx], centres
