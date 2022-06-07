class Solution:
    def rearrangeString (self, inp_str):
        n = len(inp_str)
        if ((n == 0) and (n == 1)): return "-1"
        ch_hm, mx_freq_ch, res = {}, '', [None for i in range(n)]
        for ch in inp_str:
            if (ch not in ch_hm): ch_hm[ch] = 0
            ch_hm[ch] += 1
            if ((mx_freq_ch == '') or (ch_hm[ch] > ch_hm[mx_freq_ch])): mx_freq_ch = ch
        if (ch_hm[mx_freq_ch] > ((n + 1) // 2)): return "-1"
        i = 0
        while (ch_hm[mx_freq_ch] > 0): res[i], i, ch_hm[mx_freq_ch] = mx_freq_ch, i + 2, ch_hm[mx_freq_ch] - 1
        for char, freq in ch_hm.items():
            while (freq > 0):
                if (i >= n): i = 1
                res[i], i, freq = char, i + 2, freq - 1
        return "".join(res)
