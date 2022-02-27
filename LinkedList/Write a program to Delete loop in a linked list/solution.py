'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val
'''

class Solution:
    def removeLoop (self, ll_head):
        slow_ptr, fast_ptr, prev = ll_head, ll_head, ll_head
        while ((slow_ptr.next != None) and (fast_ptr.next != None) and (fast_ptr.next.next != None)):
            slow_ptr = slow_ptr.next ; prev = fast_ptr.next ; fast_ptr = fast_ptr.next.next
            if (slow_ptr == fast_ptr):
                slow_ptr = ll_head
                while (slow_ptr != fast_ptr):
                    slow_ptr = slow_ptr.next ; prev = fast_ptr ; fast_ptr = fast_ptr.next
                prev.next = None ; break
