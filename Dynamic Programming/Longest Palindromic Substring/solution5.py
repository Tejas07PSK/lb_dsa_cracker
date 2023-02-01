class Solution:
    def longestPalindrome (self, string):
        new_str = [None for i in range((2 * len(string)) + 1)]
        j = 0
        for ch in string:
            new_str[j] = '#'
            new_str[j + 1] = ch
            j += 2
        new_str[j] = '#'
        lps = [0 for i in range(len(new_str))]
        mx_lps_cntr, mx_lps_spread = 0, 0
        i, r, c, mirr = 0, 0, 0, 0
        while (i < len(new_str)):
            mirr = 2 * c - i
            if (i < r):
                lps[i] = min(lps[mirr], (r - i))
            lt_chr = new_str[i - (lps[i] + 1)] if ((i - (lps[i] + 1)) >= 0) else '$'
            rt_chr = new_str[i + (lps[i] + 1)] if ((i + (lps[i] + 1)) < len(new_str)) else '@'
            while (lt_chr == rt_chr):
                lps[i] += 1
                lt_chr = new_str[i - (lps[i] + 1)] if ((i - (lps[i] + 1)) >= 0) else '$'
                rt_chr = new_str[i + (lps[i] + 1)] if ((i + (lps[i] + 1)) < len(new_str)) else '@'
            if ((i + lps[i]) > r): c, r = i, i + lps[i]
            if (lps[i] > mx_lps_spread):
                mx_lps_cntr, mx_lps_spread = i, lps[i]
            i += 1
        return "".join([new_str[i] for i in range((mx_lps_cntr - mx_lps_spread), (mx_lps_cntr + mx_lps_spread + 1)) if (new_str[i] != '#')])
