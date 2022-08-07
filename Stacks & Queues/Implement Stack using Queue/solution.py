def push (x):
    global queue_1
    queue_1.append(x)

def pop ():
    global queue_1, queue_2
    res = -1
    while (queue_1):
        res = queue_1.pop(0)
        if (not queue_1): break
        queue_2.append(res)
    while (queue_2): queue_1.append(queue_2.pop(0))
    return res
