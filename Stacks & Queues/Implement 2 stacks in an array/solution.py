def push1 (a, x):
    global top1
    top1 += 1 ; a[top1] = x

def push2 (a, x):
    global top2
    top2 -= 1 ; a[top2] = x

def pop1 (a):
    global top1
    if (top1 == -1) : return -1
    res = a[top1] ; a[top1] = -1 ; top1 -= 1
    return res

def pop2 (a):
    global top2
    if (top2 == len(a)): return -1
    res = a[top2] ; a[top2] = -1 ; top2 += 1
    return res
