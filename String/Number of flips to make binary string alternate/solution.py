class Solution:
    def minFlips (self, string):
        n, curr_dig = len(string), 0
        flip_cntr = 0
        for ch in string:
            if (ch != str(curr_dig)):
                flip_cntr += 1
            curr_dig = 1 & ~curr_dig
        return min(flip_cntr, (n - flip_cntr))
