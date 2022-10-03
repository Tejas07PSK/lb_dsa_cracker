from math import inf
class Solution:
    def __tot_cost_helper (self, curr_bin_state, curr_city, cost_mat):
        for next_city in range(self.n):
            mask = 1 << next_city
            if (not (curr_bin_state & mask)):
                next_bin_state = curr_bin_state | mask
                if (self.dp[next_bin_state][next_city] == inf):
                    if (next_bin_state == self.all_visited_bin_state_val): self.dp[next_bin_state][next_city] = cost_mat[next_city][0]
                    else: self.__tot_cost_helper(next_bin_state, next_city, cost_mat)
                self.dp[curr_bin_state][curr_city] = min(self.dp[curr_bin_state][curr_city], (cost_mat[curr_city][next_city] + self.dp[next_bin_state][next_city]))

    def total_cost (self, cost_mat):
        self.n = len(cost_mat)
        self.dp = [[inf for i in range(self.n)] for j in  range(2 ** self.n)]
        self.all_visited_bin_state_val = (1 << self.n) - 1
        self.__tot_cost_helper(1, 0, cost_mat)
        return (self.dp[1][0] if (self.dp[1][0] != inf) else 0)
