class Solution:
    def areIsomorphic (self, str_a, str_b):
        a, b = len(str_a), len(str_b)
        if (a != b):
            return False
        i, a_to_b, used_from_b = 0, {}, set()
        while (i < a):
            if (str_a[i] not in a_to_b):
                if (str_b[i] in used_from_b):
                    return False
                a_to_b[str_a[i]] = str_b[i]
                used_from_b.add(str_b[i])
            if (a_to_b[str_a[i]] != str_b[i]):
                return False
            i += 1
        return True
