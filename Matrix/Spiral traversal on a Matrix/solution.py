class Solution:
    def spirallyTraverse (self, matrix, r, c):
        left, right, up, down = 0, (c - 1), 0, (r - 1)
        res = []
        while ((left <= right) and (up <= down)):
            i = left
            while (i <= right):
                res.append(matrix[up][i])
                i += 1
            up += 1
            if (up > down):
                break
            i = up
            while (i <= down):
                res.append(matrix[i][right])
                i += 1
            right -= 1
            if (left > right):
                break
            i = right
            while (i >= left):
                res.append(matrix[down][i])
                i -= 1
            down -= 1
            i = down
            while (i >= up):
                res.append(matrix[i][left])
                i -= 1
            left += 1
        return res
