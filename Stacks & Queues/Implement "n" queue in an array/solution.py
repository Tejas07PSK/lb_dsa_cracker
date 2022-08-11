class NQueue:
    def __init__ (self, n, s):
        self.idx = 0
        self.next_idx_arr = [i for i in range(1, s + 1)]
        self.start = [None for i in range(n)]
        self.end = [None for i in range(n)]
        self.arr = [None for i in range(s)]

    def enqueue (self, x, m):
        m -= 1
        if (self.idx == len(self.arr)): return False
        if (self.end[m] == None):
            self.start[m] = self.idx
            self.end[m] = self.idx
        else:
            self.next_idx_arr[self.end[m]] = self.idx
            self.end[m] = self.idx
        self.arr[self.idx] = x
        self.idx = self.next_idx_arr[self.idx]
        return True

    def dequeue (self, m):
        m -= 1
        if (self.start[m] == None): return -1
        temp_idx = self.start[m]
        if (self.start[m] == self.end[m]): self.end[m], self.start[m] = None, None
        else: self.start[m] = self.next_idx_arr[self.start[m]]
        res = self.arr[temp_idx] ;self.arr[temp_idx] = None ;
        self.next_idx_arr[temp_idx] = self.idx ; self.idx = temp_idx
        return res
