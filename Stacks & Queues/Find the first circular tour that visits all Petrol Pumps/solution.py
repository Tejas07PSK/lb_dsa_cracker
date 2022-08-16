'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''

class Solution:
    def tour (self, lis, n):
        if (n < 2): return 0
        start, curr, fuel_left = 0, 0, 0
        while True:
            fuel_left += lis[curr][0]
            fuel_left -= lis[curr][1]
            curr = (curr + 1) % n
            if (fuel_left < 0):
                if (start == (n - 1)): return -1
                if (curr <= start): return -1
                start = curr
                fuel_left = 0
            elif (curr == start): break
        return start
