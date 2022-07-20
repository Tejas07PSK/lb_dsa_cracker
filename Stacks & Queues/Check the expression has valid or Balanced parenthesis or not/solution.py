from collections import deque
class Solution:
    def valid (self, string):
        if (string == ""): return False
        stk = deque()
        for ch in string:
            if ((ch == '(') or (ch == '{') or (ch == '[')): stk.append(ch)
            elif ((len(stk) == 0) or ((ch == ')') and (stk[-1] != '(')) or ((ch == '}') and (stk[-1] != '{')) or ((ch == ']') and (stk[-1] != '['))): return False
            else: stk.pop()
        return False if (len(stk) != 0) else True
