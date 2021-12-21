class Solution:
    def __rbkp_hf (self, s, sz, max_pow, max_chars):
        hv = 0
        for i in range(sz):
            hv += (ord(s[i]) * max_pow)
            max_pow //= max_chars
        return hv

    def __check_chars (self, start, end, s1, s2):
        i = 0
        while (start < end):
            if (s1[start] != s2[i]):
                return False
            start += 1 ; i += 1
        return True

    def search (self, pattern, text):
        txt_l, pt_l = len(text), len(pattern)
        if (pt_l > txt_l):
            return [-1]
        if (pt_l == txt_l):
            if (pattern == text):
                return [1]
            return [-1]
        res = []
        max_chars = 26
        max_pow = max_chars ** (pt_l - 1)
        pt_hash = self.__rbkp_hf(pattern, pt_l, max_pow, max_chars)
        roll_hash = self.__rbkp_hf(text, pt_l, max_pow, max_chars)
        if ((pt_hash == roll_hash) and self.__check_chars(0, pt_l, text, pattern)):
            res.append(1)
        for i in range(pt_l, txt_l):
            roll_hash = ((roll_hash - (ord(text[i - pt_l]) * max_pow)) * max_chars) + ord(text[i])
            if ((roll_hash == pt_hash) and self.__check_chars((i - pt_l + 1), i, text, pattern)):
                res.append(i - pt_l + 2)
        return res if (len(res) > 0) else [-1]
