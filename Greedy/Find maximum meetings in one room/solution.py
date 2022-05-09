class Solution:
    def maximumMeetings (self, n, start, end):
        if (n == 0): return 0
        meetings = [(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: x[0])
        i, j, count = 0, 1, 1
        while (j < n):
            if (meetings[j][0] > meetings[i][1]): i, count = j, count + 1
            elif (meetings[j][1] < meetings[i][1]): i = j
            j += 1
        return count
