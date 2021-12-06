import math
class Solution:
    def __pre_process (self, s, mat):
        i1, i2 = 0, 0
        j1, j2 = 0, 1
        n = len(s)
        while ((i1 < n) and (j1 < n)):
            mat[i1][j1] = True ; i1 += 1 ; j1 += 1
        while ((i2 < n) and (j2 < n)):
            mat[i2][j2] = (s[i2] == s[j2])
            i2 += 1 ; j2 += 1

    def __create_dp_mat (self, s):
        n = len(s)
        i = 0
        mat = []
        while (i < n):
            lst = []
            j = 0
            while (j < n):
                lst.append(False) ; j += 1
            mat.append(lst)
            i += 1
        self.__pre_process(s, mat)
        return mat

    def longestPalin (self, s):
        max_len_pal_so_far = -math.inf
        max_len_pal_so_far_start = -1
        max_len_pal_so_far_end = -1
        n = len(s)
        i = n - 1
        dp_mat = self.__create_dp_mat(s)
        while (i >= 0):
            j = i
            while (j < n):
                size = j - i + 1
                flag = False
                if (size < 3):
                    flag = dp_mat[i][j]
                else:
                    flag = ((s[i] == s[j]) and dp_mat[i + 1][j - 1])
                    dp_mat[i][j] = flag
                if flag:
                    if size >= max_len_pal_so_far:
                        max_len_pal_so_far = size
                        max_len_pal_so_far_start = i ; max_len_pal_so_far_end = j
                j += 1
            i -= 1
        return s[max_len_pal_so_far_start:(max_len_pal_so_far_end + 1)]
