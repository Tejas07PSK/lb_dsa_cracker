from collections import deque
class Solution:
    def __getPermutationHelper (self, i, n, k):
        while ((i < n) and (self.visited[i])): i += 1
        if (i == n):
            if (len(self.tmp_str_lst) == n): self.cntr += 1
            if (self.cntr == k): return "".join(self.tmp_str_lst)
            return ""
        self.visited[i] = True ; self.tmp_str_lst.append(str(i + 1))
        res_str = self.__getPermutationHelper(0, n, k)
        if (res_str != ""): return res_str
        self.visited[i] = False ; self.tmp_str_lst.pop()
        return self.__getPermutationHelper(i + 1, n, k)

    def getPermutation (self, n: int, k: int) -> str:
        self.visited, self.tmp_str_lst, self.cntr = [False for i in range(n)], deque(), 0
        return self.__getPermutationHelper(0, n, k)
