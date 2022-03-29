import io, os, sys
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Solution:
    def __in_order_trav_list (self, i, tree_array, n):
        left, right = (2 * i + 1), (2 * i + 2)
        if (left < n): self.__in_order_trav_list(left, tree_array, n)
        self.res.append([tree_array[i], self.res_size, False]) ; self.res_size += 1
        if (right < n): self.__in_order_trav_list(right, tree_array, n)
    
    def __count_min_swaps (self):
        self.res.sort(key=lambda x : x[0]) ; swaps = 0
        for i in range(len(self.res)):
            if (self.res[i][2]): continue
            self.res[i][2] = True
            if (self.res[i][1] == i): continue
            j = self.res[i][1]
            while (not self.res[j][2]):
                self.res[j][2] = True ; swaps += 1 ; j = self.res[j][1]
        return swaps  

    def main (self):
        self.res, self.res_size = [], 0
        tree_array = [int(i) for i in input().decode().split(' ')]
        self.__in_order_trav_list(0, tree_array, len(tree_array))
        sys.stdout.write(str(self.__count_min_swaps()))
        sys.stdout.write('\n')

Solution().main()
