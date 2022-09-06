from collections import defaultdict
from heapq import heapify, heappop, heappush

class Solution :
    def rearrangeString (self, string):
        ch_freq_hm = defaultdict(lambda : 0)
        for ch in string: ch_freq_hm[ch] -= 1
        mx_hp, res = [(val, key) for key, val in ch_freq_hm.items()], ['' for ch in string]
        heapify(mx_hp) ; i = 0
        prev_char, prev_freq = '', 0
        while (mx_hp):
            curr_freq, curr_char = heappop(mx_hp)
            res[i] = curr_char ; i += 1 ; curr_freq += 1
            if (prev_freq < 0): heappush(mx_hp, (prev_freq, prev_char))
            prev_char, prev_freq = curr_char, curr_freq
        return ''.join(res)
