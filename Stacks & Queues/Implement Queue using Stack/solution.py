def Push (x, stack1, stack2):
    stack1.append(x)

def Pop (stack1, stack2):
    if (not stack1): return -1
    while (stack1): stack2.append(stack1.pop())
    res = stack2.pop()
    while (stack2): stack1.append(stack2.pop())
    return res
