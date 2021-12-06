class Solution:
    def expand_from_cntr (self, s, l, r):
        n = len(s)
        while ((l >= 0) and (r < n) and (s[l] == s[r])):
            l -= 1 ; r += 1
        r -= 1 ; l += 1
        return (r - l + 1), l, r

    def longestPalindrome (self, s: str) -> str:
        n = len(s)
        i, start, end = 0, 0, 0
        while (i < n):
            curr_len, curr_start, curr_end = 0, 0, 0
            odd_len, odd_start, odd_end = self.expand_from_cntr(s, i, i)
            even_len, even_start, even_end  = self.expand_from_cntr(s, i, (i + 1))
            if (even_len > odd_len):
                curr_len = even_len ; curr_start = even_start ; curr_end = even_end
            else:
                curr_len = odd_len ; curr_start = odd_start ; curr_end = odd_end
            if (curr_len > (end - start + 1)):
                start = curr_start
                end = curr_end
            i += 1
        return s[start:(end + 1)]
