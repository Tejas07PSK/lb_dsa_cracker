class Solution:
    def largestRectangleInHisto (self, heights: List[str]) -> int:
        stk, i, n = [], 0, len(heights)
        res = 0
        while (i < n):
            temp_idx = i
            while (stk and (int(heights[i]) < stk[-1][1])):
                temp = stk.pop()
                res = max(res, (temp[1] * (i - temp[0])))
                temp_idx = temp[0]
            stk.append([temp_idx, int(heights[i])]) ; i += 1
        while (stk):
            res = max(res, (stk[-1][1] * (n - stk[-1][0])))
            stk.pop()
        return res

    def maximalRectangle (self, matrix: List[List[str]]) -> int:
        if (not matrix):
            return 0
        res = self.largestRectangleInHisto(matrix[0])
        i, r, c = 1, len(matrix), len(matrix[0])
        while (i < r):
            j = 0
            while (j < c):
                if (matrix[i][j] != "0"):
                    matrix[i][j] = str(int(matrix[i][j]) + int(matrix[i - 1][j]))
                j += 1
            res = max(res, self.largestRectangleInHisto(matrix[i]))
            i += 1
        return res
