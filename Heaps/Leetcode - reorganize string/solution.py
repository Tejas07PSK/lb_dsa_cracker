from collections import defaultdict
from heapq import heapify, heappop, heappush

class Solution:
    def reorganizeString (self, s: str) -> str:
        hm = defaultdict(lambda : 0)
        for ch in s: hm[ch] += 1
        hp, res, i = [(-val, key) for key, val in hm.items()], ['' for ch in s], 0
        heapify(hp)
        prev_char, prev_char_cnt = '', 0
        while (hp):
            curr_char_cnt, curr_char = heappop(hp)
            res[i] = curr_char ; i += 1 ; curr_char_cnt += 1
            if (prev_char_cnt < 0): heappush(hp, (prev_char_cnt, prev_char))
            prev_char, prev_char_cnt = curr_char, curr_char_cnt
        return "".join(res) if (i == len(s)) else ""
