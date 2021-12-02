class Solution:
    def find_common_in_rows (self, mat, r, c):
        hm = {}
        for num in mat[0]:
            hm[num] = 0
        i = 1
        res = []
        while (i < r):
            j = 0
            while (j < c):
                if ((mat[i][j] in hm) and (hm[mat[i][j]] != i)):
                    hm[mat[i][j]] += 1
                j += 1
            i += 1
        for key, value in hm.items():
            if ((value + 1) == r):
                res.append(key)
        return res
