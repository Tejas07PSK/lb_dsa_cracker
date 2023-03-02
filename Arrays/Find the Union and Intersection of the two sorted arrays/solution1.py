class Solution:
    def doUnion (self, a, n, b, m):
        a.sort() ; b.sort()
        i, j, ans = 0, 0, 0
        while ((i < n) and (j < m)):
            while (((i + 1) < n) and (a[i] == a[i + 1])): i += 1
            while (((j + 1) < m) and (b[j] == b[j + 1])): j += 1
            if (a[i] < b[j]): i += 1
            elif (a[i] > b[j]): j += 1
            else: i, j = i + 1, j + 1
            ans += 1
        while (i < n):
            while (((i + 1) < n) and (a[i] == a[i + 1])): i += 1
            i += 1
            ans += 1
        while (j < m):
            while (((j + 1) < m) and (b[j] == b[j + 1])): j += 1
            j += 1
            ans += 1
        return ans
