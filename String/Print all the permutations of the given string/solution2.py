class Solution:
    def __heap_algo (self, res, chr_lst, size):
        if (size == 1):
            res.append("".join(chr_lst))
            return
        for i in range(size):
            self.__heap_algo(res, chr_lst, (size - 1))
            if ((size & 1) == 1):
                chr_lst[0], chr_lst[size - 1] = chr_lst[size - 1], chr_lst[0]
            else:
                chr_lst[i], chr_lst[size - 1] = chr_lst[size - 1], chr_lst[i]

    def find_permutation (self, s):
        n = len(s)
        chr_lst = list(s)
        res = []
        self.__heap_algo(res, chr_lst, n)
        res.sort()
        return res
