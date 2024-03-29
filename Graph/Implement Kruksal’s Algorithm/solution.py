from heapq import heapify, heappop
from collections import deque

class Group:
    def __init__ (self, group_root_index, sum_of_edges_in_group, child_index_lst):
        self.group_root_index = group_root_index
        self.sum_of_edges_in_group = sum_of_edges_in_group
        self.child_index_lst = child_index_lst

class UnionFind:
    def __init__ (self, n, adj_lst): self.groups = [Group(i, 0, deque()) for i in range(n)]

    def __join_comps (self, src_idx, dest_idx):
        self.groups[dest_idx].sum_of_edges_in_group += self.groups[src_idx].sum_of_edges_in_group
        self.groups[src_idx].sum_of_edges_in_group = 0
        while (self.groups[src_idx].child_index_lst):
            tmp_idx = self.groups[src_idx].child_index_lst.pop()
            self.groups[tmp_idx].group_root_index = dest_idx
            self.groups[dest_idx].child_index_lst.append(tmp_idx)

    def union (self, edge):
        wt, start_idx, end_idx = edge
        if (self.__find(start_idx) != self.__find(end_idx)):
            start_idx = self.groups[start_idx].group_root_index
            end_idx = self.groups[end_idx].group_root_index
            if (len(self.groups[start_idx].child_index_lst) >= len(self.groups[end_idx].child_index_lst)):
                self.groups[end_idx].group_root_index = start_idx
                self.groups[start_idx].child_index_lst.append(end_idx)
                self.groups[start_idx].sum_of_edges_in_group += wt
                self.__join_comps(end_idx, start_idx)
                return (len(self.groups[start_idx].child_index_lst) + 1, self.groups[start_idx].sum_of_edges_in_group)
            self.groups[start_idx].group_root_index = end_idx
            self.groups[end_idx].child_index_lst.append(start_idx)
            self.groups[end_idx].sum_of_edges_in_group += wt
            self.__join_comps(start_idx, end_idx)
            return (len(self.groups[end_idx].child_index_lst) + 1, self.groups[end_idx].sum_of_edges_in_group)
        return (0, 0)

    def __find (self, idx): return self.groups[idx].group_root_index

class Solution:
    def spanningTree (self, v, adj_lst):
        uf_obj = UnionFind(v, adj_lst)
        min_heap = [(wt, i, nxt_idx) for i in range(v) for nxt_idx, wt in adj_lst[i] if (nxt_idx > i)]
        heapify(min_heap)
        while (min_heap):
            edge = heappop(min_heap)
            node_count, mst_sum = uf_obj.union(edge)
            if (node_count == v): return mst_sum
        return 0
