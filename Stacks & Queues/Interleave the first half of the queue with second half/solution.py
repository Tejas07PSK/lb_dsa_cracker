def interLeaveQueue (queue):
    n = len(queue)
    half_len = ((n + 1) // 2)
    i, tmp_arr = 0, [None for i in range(half_len)]
    while (i < half_len):
        tmp_arr[i] = queue.popleft() ; i += 1
    half_len = n - half_len ; i, j = 0, 0
    while (i < half_len):
        queue.append(tmp_arr[j]) ; j += 1
        queue.append(queue.popleft()) ; i += 1
    if (j != len(tmp_arr)):
        queue.append(tmp_arr[j]) ; j += 1
    return queue
