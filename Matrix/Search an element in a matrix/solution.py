class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = (len(matrix) - 1), (len(matrix[0]) - 1)
        up, down = 0, r
        while (up <= down):
            mid_row = up + ((down - up) // 2)
            if (target < matrix[mid_row][0]):
                down = (mid_row - 1)
            elif (target > matrix[mid_row][c]):
                up = (mid_row + 1)
            else:
                left, right = 0, c
                while (left <= right):
                    mid_col = left + ((right - left) // 2)
                    if (target < matrix[mid_row][mid_col]):
                        right = (mid_col - 1)
                    elif (target > matrix[mid_row][mid_col]):
                        left = (mid_col + 1)
                    else:
                        return (True)
                break
        return (False)
