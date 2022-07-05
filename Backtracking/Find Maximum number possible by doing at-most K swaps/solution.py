class Solution:
    def __findMaximumHelper (self, chr_arr, idx, k):
        print(chr_arr) ; print(k) ; print(idx)
        for i in range(idx, len(chr_arr)):
            curr_max = chr_arr[i]
            for j in range((i + 1), len(chr_arr)):
                if (chr_arr[j] > curr_max): curr_max = chr_arr[j]
            if (curr_max != chr_arr[i]):
                for j in range((i + 1), len(chr_arr)):
                    if (curr_max == chr_arr[j]):
                        chr_arr[i], chr_arr[j] = chr_arr[j], chr_arr[i]
                        if ((k - 1) != 0): self.__findMaximumHelper(chr_arr, i + 1, k - 1)
                        else: self.ans = max(self.ans, int("".join(chr_arr)))
                        chr_arr[i], chr_arr[j] = chr_arr[j], chr_arr[i]
                        
    def findMaximumNumber (self, string, k):
        self.ans = 0
        self.__findMaximumHelper(list(string), 0, k)
        return str(self.ans)
