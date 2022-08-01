class Solution:
    def overlappedInterval (self, intervals):
        stk = []
        intervals.sort(key=lambda x: x[0])
        for start, end in intervals:
            if (stk):
                if (start <= stk[-1][1]):
                    stk[-1][1] = max(stk[-1][1], end)
                else: stk.append([start, end])
            else: stk.append([start, end])
        return stk
