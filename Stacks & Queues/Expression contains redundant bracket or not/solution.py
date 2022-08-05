from collections import deque
class Solution:
    def __init__ (self):
        self.operators = {'+', '-', '*', '/', '^'}

    def checkRedundancy (self, expression):
        stk = deque()
        for ch in expression:
            if (ch == ')'):
                con_op = False
                while (stk[-1] != '('):
                    if (stk.pop() in self.operators): con_op = True
                if (not con_op): return 1
                stk.pop()
            else: stk.append(ch)
        return 0
