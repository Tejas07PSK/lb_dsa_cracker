from math import inf
class Solution:
    def __tot_cost_helper (self, curr_city, city_count, cost_so_far, cost_mat):
        for next_city in range(self.count):
            if (next_city not in self.visited):
                self.visited.add(next_city)
                self.__tot_cost_helper(next_city, (city_count + 1), (cost_so_far + cost_mat[curr_city][next_city]), cost_mat)
                self.visited.remove(next_city)
            elif (city_count == self.count): self.res = min(self.res, (cost_so_far + cost_mat[curr_city][0]))
        
    def total_cost (self, cost_mat):
        self.visited, self.count, self.res = set(), len(cost_mat), inf
        self.visited.add(0)
        self.__tot_cost_helper(0, 1, 0, cost_mat)
        self.visited.remove(0)
        return self.res
