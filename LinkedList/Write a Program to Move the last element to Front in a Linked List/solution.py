'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
'''

class Solution:
    def moveLastToFirst (self, head):
        prev, curr = None, head
        while (curr.next != None):
            prev = curr ; curr = curr.next
        if (prev != None):
            prev.next = None ; curr.next = head ; head = curr
        return head
