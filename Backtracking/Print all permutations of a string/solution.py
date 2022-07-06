class Solution:
    def __find_permutation_helper (self, chr_arr, idx):
        for i in range(len(chr_arr)):
            if (chr_arr[i] != ''):
                self.temp_chr_arr[idx], chr_arr[i] = chr_arr[i], ''
                if ((idx + 1) == len(chr_arr)): self.res.add("".join(self.temp_chr_arr))
                else: self.__find_permutation_helper(chr_arr, idx + 1)
                self.temp_chr_arr[idx], chr_arr[i] = '', self.temp_chr_arr[idx]

    def find_permutation (self, string):
        chr_arr = list(string)
        self.temp_chr_arr, self.res = [None for i in range(len(string))], set()
        self.__find_permutation_helper(chr_arr, 0)
        self.res = list(self.res) ; self.res.sort()
        return self.res
