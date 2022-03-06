'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

def reverseDLL (head):
    if (head == None): return head
    last, curr = None, head
    while (curr != None):
        curr.prev, curr.next = curr.next, curr.prev
        last = curr ; curr = curr.prev
    head = last
    return head
