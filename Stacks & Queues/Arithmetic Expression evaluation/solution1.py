from collections import deque
class Solution:
    def __init__ (self):
        self.table = {
            '^': 1,
            '*': 2,
            '/': 2,
            '+': 3,
            '-': 3,
            '(': 4
        }

    def InfixtoPostfix (self, string):
        stk, res = deque(), []
        for ch in string:
            if (not ch.isalpha()):
                if (ch == ')'):
                    while ((stk) and (stk[-1] != '(')): res.append(stk.pop())
                    stk.pop()
                elif (ch == '('): stk.append('(')
                else:
                    while ((stk) and (self.table[stk[-1]] <= self.table[ch])): res.append(stk.pop())
                    stk.append(ch)
            else: res.append(ch)
        while (stk): res.append(stk.pop())
        return "".join(res)
