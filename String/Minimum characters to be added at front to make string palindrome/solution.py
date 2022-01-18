class Solution:
    def computeLPS (self, string, n):
        l, i = 0, 1
        lps = [0 for i in range(n)]
        while (i < n):
            if (string[l] == string[i]):
                l += 1
                lps[i] = l
                i += 1
            else:
                if (l != 0):
                    l = lps[l - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def getMinNofCharsToBeAddedAtBegToMakeStringPalin (self, string):
        n = len(string)
        new_string = "".join(['$' if (i == n) else string[i] if (i < n) else string[n - i] for i in range(2 * n + 1)])
        m = len(new_string)
        return n - self.computeLPS(new_string, m)[m - 1]
