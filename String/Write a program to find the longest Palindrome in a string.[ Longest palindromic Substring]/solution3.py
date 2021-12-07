class Solution:
    def __pre_process (self, s):
        chr_lst = ['$']
        for ch in s:
            chr_lst.append('#') ; chr_lst.append(ch)
        chr_lst.append('#') ; chr_lst.append('@')
        return chr_lst

    def longestPalindrome (self, s: str) -> str:
        chr_lst = self.__pre_process(s)
        n = len(chr_lst)
        lps = [0 for i in range(n)]
        mx_lps, mx_lps_idx = 0, 0
        r, c, i = 1, 1, 1
        while (i < (n - 1)):
            mirr = 2 * c - i
            if (i < r):
                lps[i] = min(lps[mirr], (r - i))
            while (chr_lst[i + (1 + lps[i])] == chr_lst[i - (1 + lps[i])]):
                lps[i] += 1
            if ((lps[i] + i) > r):
                c = i
                r = lps[i] + i
            if lps[i] > mx_lps:
                mx_lps, mx_lps_idx = lps[i], i
            i += 1
        return("".join([(chr_lst[i] if chr_lst[i].isalpha() or chr_lst[i].isdigit() else '') for i in range((mx_lps_idx - mx_lps), (mx_lps_idx + mx_lps + 1))]))
