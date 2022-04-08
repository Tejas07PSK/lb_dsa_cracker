from math import ceil, log2

class TreeAncestor:
    def __init__ (self, n: int, parent: List[int]):
        self.pow_of_2_ancestor_mat = [[-1 for j in range(ceil(log2(n)) + 1)] for i in range(n)]
        self.mat_col_size = len(self.pow_of_2_ancestor_mat[0])
        self.mat_row_size = n
        for i in range(1, self.mat_row_size): self.pow_of_2_ancestor_mat[i][0] = parent[i]
        for i in range(1, self.mat_row_size):
            for j in range(1, self.mat_col_size):
                if (self.pow_of_2_ancestor_mat[i][j - 1] != -1):
                    self.pow_of_2_ancestor_mat[i][j] = self.pow_of_2_ancestor_mat[self.pow_of_2_ancestor_mat[i][j - 1]][j - 1]

    def getKthAncestor (self, node: int, k: int) -> int:
        for i in range(self.mat_col_size - 1, -1, -1):
            shift_factor = 1 << i
            if (k >= shift_factor):
                node = self.pow_of_2_ancestor_mat[node][i]
                k -= shift_factor
            if (node == -1): return -1
        return node

# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
