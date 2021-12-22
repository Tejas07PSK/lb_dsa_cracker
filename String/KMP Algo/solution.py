class Solution:
    def __form_lps_array (self, patt, patt_s):
        lps = [0 for ch in patt]
        j, i = 0, 1
        while (i < patt_s):
            if (patt[i] == patt[j]):
                lps[i] = j + 1
                j += 1 ; i += 1
            else:
                if (j != 0):
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def search (self, pattern, text):
        patt_s, t_s = len(pattern), len(text)
        if (patt_s > t_s):
            return [-1]
        if (patt_s == t_s):
            return [1] if (pattern == text) else [-1]
        i, j = 0, 0
        lps = self.__form_lps_array(pattern, patt_s)
        res = []
        while (i < t_s):
            if (text[i] == pattern[j]):
                j += 1 ; i += 1
            else:
                if (j != 0):
                    j = lps[j - 1]
                else:
                    i += 1
            if (j == patt_s):
                res.append(i - patt_s + 1)
                j = lps[j - 1]
        return res if (len(res) > 0) else [-1]
