class Solution:
    def activitySelection (self, n, start, end):
        if (n == 0): return 0
        activities = [(start[i], end[i]) for i in range(n)]
        activities.sort(key=lambda x: x[0])
        i, j, c = 0, 1, 1
        while (j < n):
            if (activities[j][0] <= activities[i][1]):
                i = i if (activities[j][1] > activities[i][1]) else j
            else: i, c = j, c + 1
            j += 1
        return c
