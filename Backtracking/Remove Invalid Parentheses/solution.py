class Solution:
    def __removeInvalidParenthesesHelper (self, i, balance_counter, chr_lst, n):
        if (i == n):
            print(chr_lst)
            if (balance_counter == 0): self.res.append("".join(chr_lst))
            return
        while ((chr_lst[i] != ')') or (chr_lst[i] != ')')): i += 1
        if (chr_lst[i] == '('): self.__removeInvalidParenthesesHelper(i + 1, balance_counter + 1, chr_lst, n)
        elif ((chr_lst[i] == ')') and ((balance_counter - 1) >= 0)): self.__removeInvalidParenthesesHelper(i + 1, balance_counter - 1, chr_lst, n)
        tmp = chr_lst[i] ; chr_lst[i] = '' ; self.__removeInvalidParenthesesHelper(i + 1, balance_counter, chr_lst, n) ; chr_lst[i] = tmp

    def removeInvalidParentheses (self, s: str) -> List[str]:
        self.res = []
        self.__removeInvalidParenthesesHelper(0, 0, list(s), len(s))
        return self.res
