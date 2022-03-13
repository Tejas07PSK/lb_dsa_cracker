'''
	# Node Class
	class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
'''

def getNthFromLast (head,n):
    i, j, win_size = head, head, 1
    while ((j != None) and (win_size < n)):
        j = j.next ; win_size += 1
    if (j == None): return -1
    while (j.next != None): i, j = i.next, j.next
    return i.data
