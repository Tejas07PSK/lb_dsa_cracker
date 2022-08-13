class MyCircularQueue:
    def __init__ (self, k: int):
        self.head, self.tail = -1, -1
        self.arr = [None for i in range(k)]
        self.size = 0

    def enQueue (self, value: int) -> bool:
        if (self.isFull()): return False
        self.tail = ((self.tail + 1) % len(self.arr))
        if (self.isEmpty()): self.head = self.tail
        self.arr[self.tail] = value ; self.size += 1
        return True

    def deQueue (self) -> bool:
        if (self.isEmpty()): return False
        self.arr[self.head] = None
        self.head = ((self.head + 1) % len(self.arr))
        self.size -= 1
        if (self.isEmpty()): self.tail = self.head = -1
        return True

    def Front (self) -> int:
        if (self.isEmpty()): return -1
        return self.arr[self.head]

    def Rear (self) -> int:
        if (self.isEmpty()): return -1
        return self.arr[self.tail]

    def isEmpty (self) -> bool: return (self.size == 0)

    def isFull(self) -> bool: return (self.size == len(self.arr))
