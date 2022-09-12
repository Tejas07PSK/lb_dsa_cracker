from collections import deque
class Solution:
    def __isCyclicHelper (self, idx, adj_lst):
        q = deque() ; q.append((idx, None))
        self.visited[idx] = True ; self.curr_bfs_trace.add(idx)
        while (q):
            node, prev_node = q.popleft()
            for vert in adj_lst[node]:
                if (not self.visited[vert]):
                    self.visited[vert] = True
                    self.curr_bfs_trace.add(vert)
                    q.append((vert, node))
                else:
                    if (vert == node): return True
                    if ((vert in self.curr_bfs_trace) and (vert != prev_node)): return True
        return False

    def isCycle (self, V, adj_lst):
        self.visited = [False for i in range(V)]
        for i in range(V):
            if (not self.visited[i]):
                self.curr_bfs_trace = set()
                res = self.__isCyclicHelper(i, adj_lst)
                if (res == True): return True
                del self.curr_bfs_trace
        return False
