class Solution:
    def __handler (self, res, chr_lst, l, r):
        if (l == (r - 1)):
            res.append("".join(chr_lst))
            return
        for i in range(l, r):
            chr_lst[l], chr_lst[i] = chr_lst[i], chr_lst[l]
            self.__handler(res, chr_lst, (l + 1), r)
            chr_lst[l], chr_lst[i] = chr_lst[i], chr_lst[l]

    def find_permutation (self, s):
        n = len(s)
        chr_lst = list(s)
        res = []
        self.__handler(res, chr_lst, 0, n)
        res.sort()
        return res
