from collections import deque
class Solution:
    def __isValid (self, par_str):
        stk = deque()
        for ch in par_str:
            if (ch == '('): stk.append(ch)
            elif (ch == ')'):
                if ((stk) and (stk[-1] == '(')): stk.pop()
                else: stk.append(ch)
        return len(stk)

    def __removeInvalidParenthesesHelper (self, i, balance_counter, chr_lst, n, min_dels_req):
        if (min_dels_req == 0):
            tmp_str = "".join(chr_lst)
            if (tmp_str in self.visited): return
            else: self.visited.add(tmp_str)
            if (self.__isValid(tmp_str) == 0): self.res.append(tmp_str)
            return
        while ((i < n) and (chr_lst[i] != ')') and (chr_lst[i] != '(')): i += 1
        for j in range(i, n):
            tmp_chr = chr_lst[j] ; chr_lst[j] = ''
            self.__removeInvalidParenthesesHelper(j + 1, balance_counter, chr_lst, n, min_dels_req - 1)
            chr_lst[j] = tmp_chr

    def removeInvalidParentheses (self, s: str) -> List[str]:
        min_dels_req = self.__isValid(s)
        self.res, self.visited = [], set()
        self.__removeInvalidParenthesesHelper(0, 0, list(s), len(s), min_dels_req)
        return self.res
