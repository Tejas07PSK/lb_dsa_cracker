def modifyQueue (q, k):
    count, tmp_stk, n = 0, [], len(q)
    while (count < k):
        tmp_stk.append(q.pop(0)) ; count += 1
    while (tmp_stk): q.append(tmp_stk.pop())
    k, count = n - k, 0
    while (count < k):
        q.append(q.pop(0)) ; count += 1
    return q
