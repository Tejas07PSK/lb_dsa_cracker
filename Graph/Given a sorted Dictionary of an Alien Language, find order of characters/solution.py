from collections import deque
class Solution:
    def findOrder (self, dct, n, k):
        adj_lst, in_deg_hm = {chr(i):set() for i in range(97, 97+k)}, {chr(i):0 for i in range(97, 97+k)}
        for i in range(n - 1):
            string_a, string_b = dct[i], dct[i + 1]
            j, k = 0, 0
            while ((j < len(string_a)) and (k < len(string_b))):
                ch_a, ch_b = string_a[j], string_b[k]
                if (ch_a != ch_b):
                    if (ch_b not in adj_lst[ch_a]):
                        adj_lst[ch_a].add(ch_b)
                        in_deg_hm[ch_b] += 1
                    break
                j += 1 ; k += 1
            if ((j < len(string_a)) and (k == len(string_b))): return ""
        q, res, n = deque(), [], len(adj_lst)
        for ch, in_deg in in_deg_hm.items():
            if (in_deg == 0): q.append(ch)
        while (q):
            curr_char = q.popleft() ; res.append(curr_char)
            for next_char in adj_lst[curr_char]:
                in_deg_hm[next_char] -= 1
                if (in_deg_hm[next_char] == 0): q.append(next_char)
        return "".join(res) if (len(res) == n) else ""
