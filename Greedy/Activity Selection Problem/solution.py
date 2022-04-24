class Solution:
    def maximumMeetings (self, n, start, end):
        if (n == 0): return 0
        meetings = [(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[0])
        i, j, c = 0, 1, 1
        while (j < n):
            if (meetings[j][0] <= meetings[i][1]):
                i = i if (meetings[j][1] > meetings[i][1]) else j
            else: i, c = j, c + 1
            j += 1
        return c
