from collections import deque
class Solution:
    def __findPathHelper (self, N, M, row, col):
        if ((row < 0) or (col < 0) or (row >= N) or (col >= N) or (M[row][col] == 0)): return
        if ((row == (N - 1)) and (col == (N - 1))):
            self.paths.append("".join(self.pth_dq)) ; return
        M[row][col] = 0
        self.pth_dq.append('D') ; self.__findPathHelper(N, M, row + 1, col) ; self.pth_dq.pop()
        self.pth_dq.append('L') ; self.__findPathHelper(N, M, row, col - 1) ; self.pth_dq.pop()
        self.pth_dq.append('R') ; self.__findPathHelper(N, M, row, col + 1) ; self.pth_dq.pop()
        self.pth_dq.append('U') ; self.__findPathHelper(N, M, row - 1, col) ; self.pth_dq.pop()
        M[row][col] = 1
        return
        
    def findPath (self, M, N):
        self.paths = [] ; self.pth_dq = deque()
        self.__findPathHelper(N, M, 0, 0)
        return self.paths
