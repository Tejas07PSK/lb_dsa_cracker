from collections import deque
class Solution:
    def evaluatePostfix (self, S):
        stk = deque()
        for ch in S:
            if (ch.isdigit()): stk.append(int(ch))
            else:
                operand2, operand1 = stk.pop(), stk.pop()
                if (ch == '*'): stk.append(operand1 * operand2)
                elif (ch == '/'): stk.append(operand1 // operand2)
                elif (ch == '+'): stk.append(operand1 + operand2)
                else: stk.append(operand1 - operand2)
        return stk.pop()
