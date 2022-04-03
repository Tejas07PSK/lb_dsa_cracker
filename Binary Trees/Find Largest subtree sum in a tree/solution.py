from math import inf
import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Solution:
    def __dfs_max_sum_sub_tree (self, root_idx, tree_arr, n):
        if ((n == 0) or (tree_arr[root_idx] == None)):
            self.max_sum = 0 ; return 0
        left_idx, right_idx = (2 * root_idx + 1), (2 * root_idx + 2)
        left_sum, right_sum = 0, 0
        if ((left_idx < n) and (tree_arr[left_idx] != None)):
            left_sum = self.__dfs_max_sum_sub_tree(left_idx, tree_arr, n)
        if ((right_idx < n) and (tree_arr[right_idx] != None)):
            right_sum = self.__dfs_max_sum_sub_tree(right_idx, tree_arr, n)
        sum_of_curr_sub_tree = left_sum + right_sum + tree_arr[root_idx]
        self.max_sum = max(self.max_sum, sum_of_curr_sub_tree)
        return sum_of_curr_sub_tree

    def main(self):
        self.max_sum = -inf
        tree_arr = [(int(ch) if (ch != 'N') else None) for ch in input().decode().split(' ') if (ch != '')]
        self.__dfs_max_sum_sub_tree(0, tree_arr, len(tree_arr))
        return self.max_sum

sys.stdout.write(str(Solution().main()) + '\n')
