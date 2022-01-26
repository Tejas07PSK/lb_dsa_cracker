class Solution:
    def transform (self, str_a, str_b):
        a, b = len(str_a), len(str_b)
        if (a != b):
            return -1
        map = {}
        i, j = 0, 0
        while ((i < a) and (j < b)):
            if (str_a[i] not in map):
                map[str_a[i]] = 0
            map[str_a[i]] += 1
            if (str_b[j] not in map):
                map[str_b[j]] = 0
            map[str_b[j]] -= 1
            i += 1
            j += 1
        for val in map.values():
            if val != 0:
                return -1
        i, j, res = a - 1, b - 1, 0
        while ((i >= 0) and (j >= 0)):
            if (str_a[i] != str_b[j]):
                i -= 1
                res += 1
            else:
                i -= 1
                j -= 1
        return res
