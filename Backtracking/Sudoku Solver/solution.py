class Solution:
    def __isValid(self, grid, row, col, number):
        for j in range(9):
            if (grid[row][j] == number): return False
        for i in range(9):
            if (grid[i][col] == number): return False
        sub_mat_start_row, sub_mat_start_col = ((row // 3) * 3), ((col // 3) * 3)
        for i in range(sub_mat_start_row, (sub_mat_start_row + 3)):
            for j in range(sub_mat_start_col, (sub_mat_start_col + 3)):
                if (grid[i][j] == number): return False
        return True

    def __solveSudokuHelper (self, row, col, grid):
        while (row < 9):
            while (col < 9):
                if (grid[row][col] == 0):
                    for number in range(1, 10):
                        if (self.__isValid(grid, row, col, number)):
                            grid[row][col] = number
                            if (self.__solveSudokuHelper(row, col + 1, grid)): return True
                            grid[row][col] = 0
                    return False
                col += 1
            col = 0
            row += 1
        return True

    def SolveSudoku (self, grid): return self.__solveSudokuHelper(0, 0, grid)

    def printGrid (self, grid):
        for i in range(9):
            for j in range(9):
                print(grid[i][j], end=' ')
