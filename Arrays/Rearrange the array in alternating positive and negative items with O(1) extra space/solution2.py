class Solution:
    def swap (self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def get_start_of_positive (self, arr, n):
        l,m,r = 0, 0, (n - 1)
        pvt = 0
        while (m <= r):
            if (arr[m] < pvt):
                self.swap(arr, l, m)
                l += 1
                m += 1
            elif (arr[m] > pvt):
                self.swap(arr, m, r)
                r -= 1
            else:
                m += 1
        return m

    def re_arrange (self, arr, n):
        j = self.get_start_of_positive(arr, n)
        i = 1
        while ((i != j) and (i < n) and (j < n)):
            self.swap(arr, i, j)
            i += 2
            j += 1
