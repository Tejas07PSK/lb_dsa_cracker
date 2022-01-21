class Solution:
    def smallestWindow(self, S, P):
        S_temp_char_map, P_char_map, n, m = {}, {}, len(S), len(P)
        match_flag = 0
        min_len, min_str = (n + 1), "-1"
        for ch in P:
            if ch not in P_char_map:
                P_char_map[ch] = 0
            P_char_map[ch] += 1
        i, j = 0, 0
        while (j < n):
            if (S[j] not in S_temp_char_map):
                S_temp_char_map[S[j]] = 0
            S_temp_char_map[S[j]] += 1
            if ((S[j] in P_char_map) and (S_temp_char_map[S[j]] <= P_char_map[S[j]])):
                match_flag += 1
            while (match_flag == m):
                temp_len = j - i + 1
                if (temp_len < min_len):
                    min_len = temp_len
                    min_str = S[i:(j + 1)]
                S_temp_char_map[S[i]] -= 1
                if ((S[i] in P_char_map) and (S_temp_char_map[S[i]] < P_char_map[S[i]])):
                    match_flag -= 1
                i += 1
            j += 1
        return min_str
