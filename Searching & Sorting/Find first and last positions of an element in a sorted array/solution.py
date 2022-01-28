class Solution:
    def binSearchWithDir (self, arr, n, key, direc):
        left, right = 0, n - 1
        loc = -1
        while (left <= right):
            mid = left + ((right - left) // 2)
            if (arr[mid] < key):
                left = mid + 1
            elif (arr[mid] > key):
                right = mid - 1
            else:
                loc = mid
                if (direc == 'l'):
                    right = mid - 1
                else:
                    left = mid + 1
        return loc

    def find (self, arr, n, x):
        first = self.binSearchWithDir(arr, n, x, 'l')
        last = -1 if (first == -1) else self.binSearchWithDir(arr, n, x, 'r')
        return [first, last]
