class Solution:
    def removeConsecutiveCharacter (self, string):
        ch_arr = list(string)
        n = len(ch_arr)
        i = 0
        while (i < n):
            j = i + 1
            while ((j < n) and (ch_arr[j] == ch_arr[i])):
                ch_arr[j] = ''
                j += 1
            i = j
        return "".join(ch_arr)
