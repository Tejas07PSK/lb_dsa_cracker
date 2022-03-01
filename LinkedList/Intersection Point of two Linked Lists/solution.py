'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

def intersetPoint (head1, head2):
    flag1, flag2 = False, False
    curr1, curr2 = head1, head2
    while ((curr1 != None) and (curr2 != None)):
        if (curr1 == curr2): return curr1.data
        if ((not flag1) and (curr1.next == None)): curr1, flag1 = head2, True
        else: curr1 = curr1.next
        if ((not flag2) and (curr2.next == None)): curr2, flag2 = head1, True
        else: curr2 = curr2.next
    return -1
