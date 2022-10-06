class Solution:
    def __isBridgeHelper (self, parent, curr_node, adj_lst, c, d):
        for next_node in adj_lst[curr_node]:
            if (next_node == parent): continue
            if (next_node not in self.visited):
                self.num += 1
                self.d[next_node], self.l[next_node] = self.num, self.num
                self.visited.add(next_node)
                if (self.__isBridgeHelper(curr_node, next_node, adj_lst, c, d)): return True
                self.l[curr_node] = min(self.l[curr_node], self.l[next_node])
            else: self.l[curr_node] = min(self.l[curr_node], self.d[next_node])
            if (((curr_node == c) and (next_node == d)) or ((curr_node == d) and (next_node == c))): return True if (self.l[next_node] > self.d[curr_node]) else False
        return False

    def isBridge (self, v, adj_lst, c, d):
        self.visited, self.num = set(), -1
        self.d, self.l = [None for i in range(v)], [None for i in range(v)]
        for i in range(v):
            if (i not in self.visited):
                self.num += 1
                self.d[i], self.l[i] = self.num, self.num
                self.visited.add(i)
                res = self.__isBridgeHelper(None, i, adj_lst, c, d)
                if (res): return 1
        return 0
