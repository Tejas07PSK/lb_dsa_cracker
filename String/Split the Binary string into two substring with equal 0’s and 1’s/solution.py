class Solution:
    def __count_consecutive (self, s, idx, n):
        cntr = 1
        while (((idx + 1) < n) and (s[idx] == s[idx + 1])):
            cntr += 1 ; idx += 1
        return cntr, (idx + 1)

    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)
        i, ans = 0, 0
        count_prev, i = self.__count_consecutive(s, i, n)
        while (i < n):
            count, i = self.__count_consecutive(s, i, n)
            ans += min(count_prev, count)
            count_prev = count
        return ans
