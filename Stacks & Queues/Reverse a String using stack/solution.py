from collections import deque
def reverse (string):
    tmp_res = [None for i in range(len(string))]
    stk = deque()
    for ch in string: stk.append(ch)
    for i in range(len(tmp_res)): tmp_res[i] = stk.pop()
    return "".join(tmp_res)
