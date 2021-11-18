class Range:
    def __init__ (self, a, b):
        self.a = a
        self.b = b

    def __lt__ (self, num):
        return True if (self.b < num) else False

    def __gt__ (self, num):
        return True if (self.a > num) else False

class Solution:
    def __swap (self, array, index1, index2):
        temp = array[index1]
        array[index1] = array[index2]
        array[index2] = temp

    def threeWayPartition (self, array, a, b):
        rng, n = Range(a, b), len(array)
        i, j, k = 0, 0, (n - 1)
        while (j <= k):
            if (rng > array[j]):
                self.__swap(array, j, i)
                i += 1
                j += 1
            elif (rng < array[j]):
                self.__swap(array, j, k)
                k -= 1
            else:
                j += 1
