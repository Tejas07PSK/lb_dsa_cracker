'''
	Your task is to remove duplicates from given 
	sorted linked list.
	
	Function Arguments: head (head of the given linked list) 
	Return Type: none, just remove the duplicates from the list.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

def removeDuplicates (head):
    prev, curr, after = None, head, None
    while (curr != None):
        if ((prev != None) and (prev.data == curr.data)):
            prev.next = curr.next ; after = curr.next
            curr.next = None ; curr = after
        else:
            prev = curr ; curr = curr.next
    return head
