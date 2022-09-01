from heapq import heappop, heappush

class Solution:
    def __init__ (self): self.mn_heap, self.mx_heap = [], []

    def balanceHeaps (self):
        balance_factor = (len(self.mn_heap) - len(self.mx_heap))
        if (balance_factor >= 1):
            if (self.mn_heap): heappush(self.mx_heap, -heappop(self.mn_heap))
        elif (balance_factor < -1):
            if (self.mx_heap): heappush(self.mn_heap, -heappop(self.mx_heap))

    def getMedian (self):
        if ((len(self.mn_heap) + len(self.mx_heap)) % 2 == 0):
            if ((self.mn_heap) and (self.mx_heap)):
                return ((-self.mx_heap[0] + self.mn_heap[0]) / 2)
        else: return -self.mx_heap[0]

    def insertHeaps (self, x):
        if (self.mx_heap):
            if (x > -self.mx_heap[0]): heappush(self.mn_heap, x)
            else: heappush(self.mx_heap, -x)
        else: heappush(self.mx_heap, -x)
        self.balanceHeaps()
