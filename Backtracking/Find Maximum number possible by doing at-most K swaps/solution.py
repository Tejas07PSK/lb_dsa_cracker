class Solution:
    def __findMaximumHelper (self, chr_arr, i, k):
        if ((i == len(chr_arr)) or (k ==0)): return
        curr_max = chr_arr[i]
        for j in range((i + 1), len(chr_arr)):
            if (chr_arr[j] > curr_max): curr_max = chr_arr[j]
        if (curr_max != chr_arr[i]):
            for j in range((i + 1), len(chr_arr)):
                if (curr_max == chr_arr[j]):
                    chr_arr[i], chr_arr[j] = chr_arr[j], chr_arr[i]
                    self.ans = max(self.ans, int("".join(chr_arr)))
                    self.__findMaximumHelper(chr_arr, i + 1, k - 1)
                    chr_arr[i], chr_arr[j] = chr_arr[j], chr_arr[i]
        else: self.__findMaximumHelper(chr_arr, i + 1, k)

    def findMaximumNum (self, string, k):
        self.ans = int(string)
        self.__findMaximumHelper(list(string), 0, k)
        return str(self.ans)
