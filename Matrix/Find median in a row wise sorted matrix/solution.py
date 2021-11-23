class Solution:
    def __getMinMax (self, matrix, r, c):
        i, min_element, max_element = 1, matrix[0][0], matrix[0][c - 1]
        while (i < r):
            min_element = min(min_element, matrix[i][0])
            max_element = max(max_element, matrix[i][c - 1])
            i += 1
        return min_element, max_element

    def __getNoOfElesLtTarget (self, matrix, row, c, target):
        l, r = 0, (c - 1)
        while (l <= r):
            mid = l + ((r - l) // 2)
            if (matrix[row][mid] > target):
                r = mid - 1
            else:
                l = mid + 1
        return l

    def median (self, matrix, r, c):
        min_element, max_element = self.__getMinMax(matrix, r, c)
        half = (r * c + 1) // 2
        while (min_element <= max_element):
            mid_element = min_element + ((max_element - min_element) // 2)
            count, i = 0, 0
            while (i < r):
                count += self.__getNoOfElesLtTarget(matrix, i, c, mid_element)
                i += 1
            if (count >= half):
                max_element = mid_element - 1
            else:
                min_element = mid_element + 1
        return min_element
