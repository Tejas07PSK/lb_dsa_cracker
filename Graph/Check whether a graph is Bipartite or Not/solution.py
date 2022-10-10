from collections import deque
class Solution:
    def __bfs_bipart_helper (self, start_node, lvl_cntr, adj_lst):
        self.even_visited.add(start_node)
        q = deque() ; q.append(start_node)
        while (q):
            curr_sz = len(q)
            while (curr_sz > 0):
                curr_node = q.popleft()
                for next_node in adj_lst[curr_node]:
                    if ((lvl_cntr + 1) % 2 == 0):
                        if (next_node in self.odd_visited): return False
                        if (next_node not in self.even_visited):
                            self.even_visited.add(next_node)
                            q.append(next_node)
                    else:
                        if (next_node in self.even_visited): return False
                        if (next_node not in self.odd_visited):
                            self.odd_visited.add(next_node)
                            q.append(next_node)
                curr_sz -= 1
            lvl_cntr += 1
        return True

    def isBipartite (self, v, adj_lst):
        self.even_visited, self.odd_visited = set(), set()
        for i in range(v):
            if ((i not in self.even_visited) and (i not in self.odd_visited)):
                if (not self.__bfs_bipart_helper(i, 0, adj_lst)): return False
        return True
