def rev (q):
    if (q.empty()): return q
    ele = q.get_nowait()
    q = rev(q)
    q.put_nowait(ele)
    return q
