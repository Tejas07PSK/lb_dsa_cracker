import math
class Line:
    def __init__ (self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def getY (self, x):
        return -1 * (((self.a * x) + self.c) / self.b)

class Point:
    def __init__ (self, x, y):
        self.x, self.y = x, y

    def __sub__ (self, pt):
        return math.sqrt(((self.x - pt.x) ** 2) + ((self.y - pt.y) ** 2))

class Solution:
    def __sumOfDistancesOfPointFromOtherPoints (self, point_list, point):
        tot_dist = 0
        for pt in point_list:
            tot_dist += (pt - point)
        return tot_dist

    def __ternarySearchPoint (self, point_list, l):
        low, high, acc =  -1e6, 1e6, 1e-6 + 1
        while ((high - low) > acc):
            mid1 = low + ((high - low) / 3)
            mid2 = high - ((high - low) / 3)
            d1 = self.__sumOfDistancesOfPointFromOtherPoints(point_list, Point(mid1, l.getY(mid1)))
            d2 = self.__sumOfDistancesOfPointFromOtherPoints(point_list, Point(mid2, l.getY(mid2)))
            if (d1 < d2):
                high = mid2
            else:
                low = mid1
        x = (low + high) / 2
        y = l.getY(x)
        return Point(x, y)

    def getMinDistance (self, list_of_coordinates, line_coeffs):
        point_list = [Point(c[0], c[1]) for c in list_of_coordinates]
        l = Line(line_coeffs[0], line_coeffs[1], line_coeffs[2])
        return self.__sumOfDistancesOfPointFromOtherPoints(point_list, self.__ternarySearchPoint(point_list, l))
