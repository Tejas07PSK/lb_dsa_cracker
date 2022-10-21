import io, os, sys
from collections import deque
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
n = int(input().decode())
adj_lst = [[] for i in range(n + 1)]
in_time = [0 for i in range(n + 1)]
out_time = [0 for i in range(n + 1)]
visited = [False for i in range(n + 1)]
for i in range(n - 1):
    start, end = map(int, input().decode().split())
    adj_lst[start].append(end)
stk = deque([1]) ; time = -1
while (stk):
    curr_node = stk[0]
    if (not visited[curr_node]):
        time += 1 ; in_time[curr_node] = time
        visited[curr_node] = True
        for next_node in adj_lst[curr_node]: stk.appendleft(next_node)
    else:
        time += 1 ; out_time[curr_node] = time
        stk.popleft()
def __chk (node_1, node_2):
    global in_time, out_time
    return ((in_time[node_2] > in_time[node_1]) and (out_time[node_2] < out_time[node_1]))
q = int(input().decode())
for i in range(q):
    direc, x, y = map(int, input().decode().split())
    if (direc == 0):
        sys.stdout.write("YES\n" if (__chk(x, y)) else "NO\n")
    else:
        sys.stdout.write("YES\n" if (__chk(y, x)) else "NO\n")
