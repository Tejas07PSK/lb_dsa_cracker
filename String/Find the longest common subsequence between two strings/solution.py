class Solution:
    def lcs (l1, l2, s1, s2):
        tab = [[0 for i in range(l2 + 1)] for j in range(l1 + 1)]
        i = l2 - 1
        while (i >= 0):
            j = l1 - 1
            while (j >= 0):
                if (s1[j] == s2[i]):
                    tab[i][j] = 1 + tab[i + 1][j + 1]
                else:
                    tab[i][j] = max(tab[i][j + 1], tab[i + 1][j])
                j -= 1
            i -= 1
        return tab[0][0]
