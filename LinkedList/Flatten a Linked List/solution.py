'''
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
'''

def flatten(head):
    ptr = head ; ptr = ptr.next
    while (ptr != None):
        prev, curr1, curr2 = None, head, ptr
        while ((curr1 != None) and (curr2 != None)):
            if (curr1.data <= curr2.data):
                if (prev == None): head = curr1
                else: prev.bottom = curr1
                prev = curr1 ; curr1 = curr1.bottom
            else:
                if (prev == None): head = curr2
                else: prev.bottom = curr2
                prev = curr2 ; curr2 = curr2.bottom
        if (curr1 != None): prev.bottom = curr1
        if (curr2 != None): prev.bottom = curr2
        ptr = ptr.next
    return head
