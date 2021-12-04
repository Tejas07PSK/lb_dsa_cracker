class Solution:
    def isPalindrome (self, s):
        i, j = 0, len(s) - 1
        while (i < j):
            if (s[i] != s[j]):
                return 0
            i += 1 ; j -= 1
        return 1
