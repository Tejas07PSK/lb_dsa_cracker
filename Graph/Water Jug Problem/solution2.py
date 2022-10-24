class Solution:
    def minSteps (self, m, n, d):
        if (m < n): m, n = n, m
        a, b, gcd = m, n, 0
        while (b != 0): a, b = b, a % b
        gcd = a
        if ((d % gcd) == 0):
            a, b, res1 = m, 0, 1
            while ((a != d) and (b != d)):
                qty = min(a, n - b)
                a -= qty
                b += qty
                res1 += 1
                if ((a == d) or (b == d)): break
                if (a == 0): a, res1 = m, res1 + 1
                if (b == n): b, res1 = 0, res1 + 1
            res = res1
            a, b, res1 = n, 0, 1
            while ((a != d) and (b != d)):
                qty = min(a, m - b)
                a -= qty
                b += qty
                res1 += 1
                if ((a == d) or (b == d)): break
                if (a == 0): a, res1 = n, res1 + 1
                if (b == m): b, res1 = 0, res1 + 1
            return min(res, res1)
        return -1
