class MyStack:

    def __init__(self): self.arr, self.idx = [None for i in range(50)], -1

    def peek (self): return self.arr[self.idx]

    def size (self): return self.idx + 1

    def push (self, data):
        if ((self.idx + 1) >= len(self.arr)):
            tmp_arr = [None for i in range(2 * len(self.arr))]
            for i in range(len(self.arr)): tmp_arr[i] = self.arr[i]
            self.arr = tmp_arr
        self.arr[self.idx + 1], self.idx = data, self.idx + 1

    def pop(self):
        if (self.size() == 0): return -1
        number, self.arr[self.idx], self.idx = self.arr[self.idx], None, self.idx - 1
        return number
