from collections import deque
class Solution:
    def minSteps (self, m, n, d):
        visited = set()
        q = deque()
        q.append(((0, 0), 0))
        visited.add((0, 0))
        while (q):
            curr_state, steps = q.popleft()
            curr_jug1_cntnt, curr_jug2_cntnt = curr_state
            next_states = [(0, curr_jug2_cntnt), (curr_jug1_cntnt, 0),
            (m, curr_jug2_cntnt), (curr_jug1_cntnt, n),
            (curr_jug1_cntnt + min(curr_jug2_cntnt, m - curr_jug1_cntnt), curr_jug2_cntnt - min(curr_jug2_cntnt, m - curr_jug1_cntnt)),
            (curr_jug1_cntnt - min(curr_jug1_cntnt, n - curr_jug2_cntnt), curr_jug2_cntnt + min(curr_jug1_cntnt, n - curr_jug2_cntnt))]
            for next_state in next_states:
                if (next_state not in visited):
                    if ((next_state[0] == d) or (next_state[1] == d)): return steps + 1
                    visited.add(next_state)
                    q.append((next_state, steps + 1))
        return -1
