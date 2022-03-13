'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

class Solution:
    def compute (self, head):
        if ((head == None) or (head.next == None)): return head
        ptr = compute(head.next)
        if (head.data < ptr.data):
            head.next = None ; head = ptr
        else: head.next = ptr
        return head
