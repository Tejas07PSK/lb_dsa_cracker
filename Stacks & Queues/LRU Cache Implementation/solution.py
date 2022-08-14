class Node:
    def __init__ (self, key, data): self.data, self.key, self.prev, self.next = data, key, None, None

class LRUCache:
    def __init__ (self, cap):
        self.head, self.tail = None, None
        self.hm, self.count, self.limit = {}, 0, cap

    def get (self, key):
        if (key not in self.hm): return -1
        tmp_node = self.hm[key]
        if (tmp_node != self.tail):
            if (tmp_node.prev != None): tmp_node.prev.next = tmp_node.next
            else: self.head = tmp_node.next
            tmp_node.next.prev = tmp_node.prev
            tmp_node.prev = self.tail
            tmp_node.next = None
            self.tail.next = tmp_node
            self.tail = tmp_node
        return tmp_node.data

    def set (self, key, value):
        if (key not in self.hm):
            if (self.count == self.limit):
                self.count -= 1
                if (self.head == self.tail):
                    tmp_key = self.head.key
                    del self.head ; del self.hm[tmp_key]
                    self.head = self.tail = None
                else:
                    tmp_node, tmp_key = self.head, self.head.key
                    self.head = self.head.next ; self.head.prev = None
                    del tmp_node ; del self.hm[tmp_key]
            self.count += 1
            if (self.tail == None): self.head = self.tail = Node(key, value)
            else:
                self.tail.next = Node(key, value)
                self.tail.next.prev = self.tail
                self.tail = self.tail.next
            self.hm[key] = self.tail
        else:
            tmp_node = self.hm[key]
            tmp_node.data = value
            if (tmp_node != self.tail):
                if (tmp_node.prev != None): tmp_node.prev.next = tmp_node.next
                else: self.head = tmp_node.next
                tmp_node.next.prev = tmp_node.prev
                tmp_node.prev = self.tail
                tmp_node.next = None
                self.tail.next = tmp_node
                self.tail = tmp_node
