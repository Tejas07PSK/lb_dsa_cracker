class Solution:
    def rowWithMax1s (self, arr, n, m):
        max_no_of_ones_so_far, row_with_max_ones = 0, -1
        i, j = 0, (m - 1)
        while (i <= (n - 1)):
            if (arr[i][j] == 1):
                while (((j - 1) >= 0) and (arr[i][j - 1] == 1)):
                    j -= 1
                no_of_ones = m - j
                if (no_of_ones == m):
                    return i
                if (no_of_ones > max_no_of_ones_so_far):
                    max_no_of_ones_so_far, row_with_max_ones = no_of_ones, i
            i += 1
        return row_with_max_ones
