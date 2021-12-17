class Solution:
    def ispar (self, s):
        stk = []
        for ch in s:
            if ((ch == '(') or (ch == '{') or (ch == '[')):
                stk.append(ch)
            elif ((ch == ')') or (ch == '}') or (ch == ']')):
                if (len(stk) == 0):
                    return False
                elif (((ch == ')') and (stk[-1] == '(')) or ((ch == '}') and (stk[-1] == '{')) or ((ch == ']') and (stk[-1] == '['))):
                    stk.pop()
                else:
                    return False
        return True if (len(stk) == 0) else False
