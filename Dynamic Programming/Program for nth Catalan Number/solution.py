class Solution:
    def findCatalan (self, n):
        if ((n == 0) or (n == 1)): return 1
        nume, denom = 1, 1
        for i in range(2, n + 1):
            nume *= (4 * i - 2)
            denom *= (i + 1)
        return (nume // denom)
