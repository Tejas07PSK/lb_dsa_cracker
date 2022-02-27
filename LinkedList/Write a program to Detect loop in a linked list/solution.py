'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''

class Solution:
    def detectLoop (self, ll_head):
        slow_ptr, fast_ptr = ll_head, ll_head
        while ((slow_ptr.next != None) and (fast_ptr.next != None) and (fast_ptr.next.next != None)):
            slow_ptr = slow_ptr.next ; fast_ptr = fast_ptr.next.next
            if (slow_ptr == fast_ptr): return True
        return False
