class Solution:
    def vertexCover (self, n: int, m: int, edges: List[List[int]]) -> int:
        low, high = 1, n
        lim = 1 << n
        adj_lst = [[] for i in range(n)]
        for start, end in edges:
            adj_lst[start - 1].append(end - 1)
            adj_lst[end - 1].append(start - 1)
        while (low < high):
            mid = (low + high) >> 2
            curr_set_state = ((1 << mid) - 1)
            res = False
            while (curr_set_state < lim):
                visited = [set() for i in range(n)]
                edg_cnt, count, mask, set_bit_cntr = m, 0, 1, 0
                while (set_bit_cntr < mid):
                    if ((curr_set_state & mask) > 0):
                        set_bit_cntr += 1
                        for next_idx in adj_lst[count]:
                            if (next_idx not in visited[count]):
                                edg_cnt -= 1 ; visited[count].add(next_idx)
                                visited[next_idx].add(count)
                    count += 1
                    mask <<= 1
                if (edg_cnt == 0):
                    res = True ; break
                c = curr_set_state & -curr_set_state
                r = curr_set_state + c
                curr_set_state = (((r ^ curr_set_state) >> 2) // c) | r
                del visited
            if (res == True): high = mid
            else: low = mid + 1
        return low
