class Solution:
    def intersection (self, a: List[int], b: List[int]) -> List[int]:
        n, m = len(a), len(b)
        a.sort() ; b.sort()
        i, j, ans = 0, 0, []
        while ((i < n) and (j < m)):
            while (((i + 1) < n) and (a[i] == a[i + 1])): i += 1
            while (((j + 1) < m) and (b[j] == b[j + 1])): j += 1
            if (a[i] < b[j]): i += 1
            elif (a[i] > b[j]): j += 1
            else:
                ans.append(a[i])
                i, j = i + 1, j + 1
        return ans
