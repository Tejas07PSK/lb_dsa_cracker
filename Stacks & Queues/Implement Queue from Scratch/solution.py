class MyQueue:

    def __init__ (self): self.arr, self.start, self.end = [None for i in range(50)], -1, -1

    def printInternals (self):
        print((self.start, self.end)) ; print(self.arr)

    def capacity (self): return len(self.arr)

    def peek (self): return self.arr[self.start]

    def size (self):
        if (self.end < self.start): return (self.end + 1) + (len(self.arr) - self.start)
        if (self.end == -1): return 0
        return self.end - self.start + 1

    def push (self, data):
        if (self.end == -1): self.start, self.end = self.start + 1, self.end + 1
        elif (((self.end + 1) % len(self.arr)) == self.start):
            temp = [None for i in range(2 * len(self.arr))]
            if (self.end >= self.start):
                for i in range(len(self.arr)): temp[i] = self.arr[i]
                self.end = len(self.arr)
            else:
                idx = 0
                for i in range(self.start, len(self.arr)):
                    temp[idx] = self.arr[i] ; idx += 1
                for i in range(0, self.end + 1):
                    temp[idx] = self.arr[i] ; idx += 1
                self.end = idx
            self.start, self.arr = 0, temp
        else: self.end = (self.end + 1) % len(self.arr)
        self.arr[self.end] = data

    def pop (self):
        if (self.size() == 0): return -1
        res = self.arr[self.start]
        self.arr[self.start] = None
        if (self.start == self.end): self.end, self.start = -1, -1
        else: self.start = (self.start + 1) % len(self.arr)
        return res
