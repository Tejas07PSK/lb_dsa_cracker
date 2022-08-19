from collections import deque
def printFirstNegativeInteger (A, N, K):
    q = deque()
    for i in range(K):
        if (A[i] < 0): q.append(A[i])
    i, j, res = 1, K, [q[0] if q else 0]
    while (j < N):
        if (A[i - 1] < 0) and (q): q.popleft()
        if (A[j] < 0): q.append(A[j])
        res.append(q[0] if q else 0)
        i += 1 ; j += 1
    return res
