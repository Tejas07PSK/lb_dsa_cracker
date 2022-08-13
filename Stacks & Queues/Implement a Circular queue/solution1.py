class Node:
    def __init__ (self, data): self.data, self.next = data, None

class MyCircularQueue:
    def __init__ (self, k: int):
        self.head, self.tail = None, None
        self.size, self.limit = 0, k

    def enQueue (self, value: int) -> bool:
        if (self.isFull()): return False
        if (self.isEmpty()): self.tail = self.head = Node(value)
        else:
            self.tail.next = Node(value) ; self.tail = self.tail.next
        self.tail.next = self.head ; self.size += 1
        return True

    def deQueue (self) -> bool:
        if (self.isEmpty()): return False
        temp = self.head ; self.head = self.head.next
        self.tail.next = self.head ; self.size -= 1
        temp.next = None; del temp
        if (self.isEmpty()): self.tail = None
        return True

    def Front (self) -> int:
        if (self.isEmpty()): return -1
        return self.head.data

    def Rear (self) -> int:
        if (self.isEmpty()): return -1
        return self.tail.data

    def isEmpty (self) -> bool: return (self.size == 0)

    def isFull(self) -> bool: return (self.size == self.limit)
