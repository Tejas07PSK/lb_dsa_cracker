class KStacksInAnArray:
    def __init__ (self, k, n):
        self.arr = [None for i in range(n)]
        self.tops = [-1 for i in range(k)]
        self.prev_nxt = [(i + 1) for i in range(n)]
        self.idx = 0

    def __resize (self):
        tmp_arr = [None for i in range(2 * len(self.arr))]
        tmp_prev_nxt = [(i + 1) for i in range(2 * len(self.prev_nxt))]
        for i in range(n):
            tmp_arr[i] = self.arr[i]
            tmp_prev_nxt[i] = self.prev_nxt[i]
        self.arr, tmp_arr = tmp_arr, self.arr
        self.prev_nxt, tmp_prev_nxt = tmp_prev_arr, self.prev_nxt
        del tmp_arr, tmp_prev_nxt

    def push (self, data, stack_number):
        if (self.idx == len(self.arr)): self.__resize()
        self.arr[self.idx] = data
        nxt_idx_holder = self.prev_nxt[self.idx]
        self.prev_nxt[self.idx] = self.tops[stack_number]
        self.tops[stack_number] = self.idx
        self.idx = nxt_idx_holder

    def pop (self, stack_number):
        if (self.tops[stack_number] == -1): return -1
        res = self.arr[self.tops[stack_number]]
        self.arr[self.tops[stack_number]] = None
        prev_idx_holder = self.prev_nxt[self.tops[stack_number]]
        self.prev_nxt[self.tops[stack_number]] = self.idx
        self.idx = self.tops[stack_number]
        self.tops[stack_number] = prev_idx_holder
        return res
