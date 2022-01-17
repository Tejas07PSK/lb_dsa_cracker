import heapq as hq
class Solution:
    def rearrangeString (self, string):
        dct = {}
        n = len(string)
        for ch in string:
            if ch not in dct:
                dct[ch] = 0
            dct[ch] -= 1
        if (len(dct) == 1):
            return ""
        heap = [[val, key] for key, val in dct.items()]
        hq.heapify(heap)
        if (-heap[0][0] > ((n + 1) // 2)):
            return ""
        i, res = 0, [None for j in range(n)]
        prev_node, node = None, None
        while (i < n):
            prev_node = hq.heappop(heap)
            res[i] = prev_node[1]
            prev_node[0] += 1
            i += 1
            if (i == n):
                break
            node = hq.heappop(heap)
            res[i] = node[1]
            node[0] += 1
            i += 1
            hq.heappush(heap, node)
            hq.heappush(heap, prev_node)
        return "".join(res)
