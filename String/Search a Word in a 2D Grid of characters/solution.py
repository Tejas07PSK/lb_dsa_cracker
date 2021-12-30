class Solution:
    def __compare_direction_substring (self, i, j, k, offset_row, offset_col, n, grid, word):
        while (k < n):
            if (grid[i][j] != word[k]):
                return False
            i += offset_row ; j += offset_col ; k += 1
        return True

    def searchWord (self, grid, word):
        r, c, n = len(grid), len(grid[0]), len(word)
        offsets = ((0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1))
        idx_within_range = lambda idx, start, end : start <= idx < end
        res = []
        for i in range(r):
            for j in range(c):
                if (grid[i][j] == word[0]):
                    for offset_row, offset_col in offsets:
                        end_pos_row, end_pos_col = (i + ((n - 1) * offset_row)), (j + ((n - 1) * offset_col))
                        if (idx_within_range(end_pos_row, 0, r) and idx_within_range(end_pos_col, 0, c)):
                            if (self.__compare_direction_substring((i + offset_row), (j + offset_col), 1, offset_row, offset_col, n, grid, word)):
                                res.append([i, j])
                                break
        return res
