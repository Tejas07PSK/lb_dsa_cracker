import io, os, sys
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

class Solution:
    def __dfs_no_loop (self, root, adj_matrix, no_of_nodes):
        self.visited.add(root) ; i = 0
        while (i < no_of_nodes):
            if (adj_matrix[root][i] == 1):
                if (i not in self.visited):
                    if (not self.__dfs_no_loop(i, adj_matrix, no_of_nodes)): return False
                else: return False
            i += 1
        return True

    def __isGraphTree (self, root, adj_matrix, no_of_nodes):
        self.visited = set()
        if (self.__dfs_no_loop(root, adj_matrix, no_of_nodes) and (len(self.visited) == no_of_nodes)):
            return True
        return False

    def main (self):
        no_of_nodes, root = map(int, input().decode().split(' '))
        adj_matrix = [list(map(int, input().decode().split(' '))) for i in range(no_of_nodes)]
        return self.__isGraphTree(root, adj_matrix, no_of_nodes)

sys.stdout.write(str(Solution().main()) + '\n')
