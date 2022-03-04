#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None

def isCircular (head):
    if (head == None): return True
    slow_ptr, fast_ptr = head, head
    while ((fast_ptr.next != None) and (fast_ptr.next.next != None)):
        slow_ptr, fast_ptr = slow_ptr.next, fast_ptr.next.next
        if (slow_ptr == fast_ptr): return True
    return False
