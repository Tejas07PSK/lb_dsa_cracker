class Node:
    def __init__ (self, data): self.data, self.prev, self.next = data, None, None

class Deque:
    def __init__ (self): self.head, self.tail = None, None

    def pop (self):
        if (self.tail == None): return -1
        temp = self.tail
        self.tail = self.tail.prev
        if (self.tail != None): self.tail.next = None
        else: self.head = self.tail
        res = temp.data
        del temp
        return res

    def pop_left (self):
        if (self.head == None): return -1
        temp = self.head
        self.head = self.head.next
        if (self.head != None): self.head.prev = None
        else: self.tail = self.head
        res = temp.data
        del temp
        return res

    def push (self, data):
        if (self.tail == None):
            self.tail = Node(data)
            self.head = self.tail
        else:
            self.tail.next = Node(data)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def push_left (self, data):
        if (self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            self.head.prev = Node(data)
            self.head.prev.next = self.head
            self.head = self.head.prev

class Stack1:
    def __init__ (self): self.dq = Deque()

    def push (self, data): self.dq.push(data)

    def pop (self): return self.dq.pop()

class Stack2:
    def __init__ (self): self.dq = Deque()

    def push (self, data): self.dq.push_left(data)

    def pop (self): return self.dq.pop_left()
