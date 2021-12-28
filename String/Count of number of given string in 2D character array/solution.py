class Solution:
    def dfs_search (self, curr_word_idx, curr_mat_row, curr_mat_col, r, c, n, word, matrix):
        res = 0
        if ((curr_mat_row >= 0 and curr_mat_row < r) and (curr_mat_col >= 0 and curr_mat_col < c) and (word[curr_word_idx] == matrix[curr_mat_row][curr_mat_col])):
            temp = word[curr_word_idx]
            matrix[curr_mat_row][curr_mat_col] = '0'
            curr_word_idx += 1
            if (curr_word_idx == n):
                res = 1
            else:
                res += self.dfs_search(curr_word_idx, curr_mat_row, (curr_mat_col + 1), r, c, n, word, matrix)
                res += self.dfs_search(curr_word_idx, curr_mat_row, (curr_mat_col - 1), r, c, n, word, matrix)
                res += self.dfs_search(curr_word_idx, (curr_mat_row + 1), curr_mat_col, r, c, n, word, matrix)
                res += self.dfs_search(curr_word_idx, (curr_mat_row - 1), curr_mat_col, r, c, n, word, matrix)
            matrix[curr_mat_row][curr_mat_col] = temp
        return res

    def findOccurrence(self,mat,target):
        r, c, n = len(mat), len(mat[0]), len(target)
        res = 0
        for i in range(r):
            for j in range(c):
                res += self.dfs_search(0, i, j, r, c, n, target, mat)
        return res
