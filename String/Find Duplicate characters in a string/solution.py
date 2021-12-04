class Solution:
    def findDuplicates (self, s):
        res, visited = set(), set()
        i, n = 0, len(s)
        while (i < n):
            if s[i] not in visited:
                visited.add(s[i])
            else:
                res.add(s[i])
            i += 1
        return res
