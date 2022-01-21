class Solution:
    def removeConsecutiveCharacter (self, string):
        ch_arr = list(string)
        n = len(ch_arr)
        i, j = 0, 1
        self.removeConsecutiveCharacterHelper(i, j, ch_arr, n)
        return "".join(ch_arr)

    def removeConsecutiveCharacterHelper (self, i, j, ch_arr, n):
        if (j == n):
            return
        if (ch_arr[j] == ch_arr[i]):
            ch_arr[j] = ''
        else:
            i = j
        j += 1
        self.removeConsecutiveCharacterHelper(i, j, ch_arr, n)
