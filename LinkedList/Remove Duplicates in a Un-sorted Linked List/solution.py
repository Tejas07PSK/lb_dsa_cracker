'''
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	
'''

class Solution:
    def removeDuplicates (self, head):
        prev, curr, after = None, head, None
        seen = set()
        while (curr != None):
            if (curr.data in seen):
                after = curr.next ; prev.next = after
                curr.next = None ; curr = after
            else:
                seen.add(curr.data)
                prev = curr ; curr = curr.next
        return head
