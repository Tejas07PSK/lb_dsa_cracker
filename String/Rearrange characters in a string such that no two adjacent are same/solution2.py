class Solution:
    def rearrangeString (self, string):
        dct, n = {}, len(string)
        max_char, max_char_freq = '', 0
        for ch in string:
            if ch not in dct:
                dct[ch] = 0
            dct[ch] += 1
            if (dct[ch] > max_char_freq):
                max_char_freq, max_char = dct[ch], ch
        if ((len(dct) == 1) or (max_char_freq > ((n + 1) // 2))):
            return ""
        i, res = 0, [None for j in range(n)]
        while (dct[max_char] > 0):
            res[i] = max_char
            dct[max_char] -= 1
            i += 2
        del dct[max_char]
        for ch, freq in dct.items():
            while (freq > 0):
                if (i >= n):
                    i = 1
                res[i] = ch
                freq -= 1
                i += 2
        return "".join(res)
