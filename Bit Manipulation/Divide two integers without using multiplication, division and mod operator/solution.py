class Solution:
    def divide (self, a, b):
        if (a == 0): return 0
        if (b == 0): return -1
        sign = 1
        if (a < 0):
            a = -a
            sign = -sign
        if (b < 0):
            b = -b
            sign = -sign
        if (a == b): return sign
        quo = 0
        while (a >= b):
            x = 0
            while ((a - (b << x)) >= 0): x += 1
            x -= 1
            quo += 1 << x
            a -= (b << x)
        return (~quo + 1) if (sign < 0) else quo
