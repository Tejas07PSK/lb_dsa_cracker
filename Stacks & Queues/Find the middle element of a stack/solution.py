class DLLNode:
    def __init__ (self, data): self.data, self.prev, self.next = data, None, None

class MidOpStack:
    def __init__ (self): self.head, self.mid, self.tail, self.size = None, None, None, 0

    def push (self, data):
        if (self.head == None):
            self.head = DLLNode(data)
            self.tail = self.head
        else:
            self.tail.next = DLLNode(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
        self.size += 1
        if ((self.size % 2) == 1):
            if (self.mid == None): self.mid = self.head
            else: self.mid = self.mid.next

    def pop (self):
        if (self.tail == None): return -1
        res = self.tail
        if (self.tail.prev != None): self.tail.prev.next = None
        self.tail = self.tail.prev
        res.prev = None
        self.size -= 1
        if ((self.size % 2) == 0): self.mid = self.mid.prev
        if (self.tail == None): self.head = None
        temp = res.data ; del res
        return temp

    def getMiddle (self): return self.mid.data if (self.mid != None) else -1

    def getHead (self): return self.head.data if (self.head != None) else -1

    def getTail (self): return self.tail.data if (self.head != None) else -1

    def deleteMiddle (self):
        if (self.mid == None): return -1
        res = self.mid
        if (self.mid.prev != None): self.mid.prev.next = self.mid.next
        if (self.mid.next != None): self.mid.next.prev = self.mid.prev
        self.size -= 1
        if ((self.size % 2) == 0): self.mid = self.mid.prev
        else: self.mid = self.mid.next
        if (self.mid == None): self.head, self.tail = None, None
        elif (res == self.head): self.head = self.mid
        res.next, res.prev = None, None
        temp = res.data ; del res
        return temp
