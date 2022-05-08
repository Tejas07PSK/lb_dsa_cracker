from math import ceil
class Solution:
    def minimumDays (self, S, N, M):
        return ceil((S * M) / N) if ((N >= M) and ((S < 7) or ((N * 6) >= (M * 7)))) else -1
