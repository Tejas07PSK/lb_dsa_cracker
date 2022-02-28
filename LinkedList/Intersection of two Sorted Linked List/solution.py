''' structure of node:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''

def findIntersection (head1, head2):
    prev, head = None, None
    while ((head1 != None) and (head2 != None)):
        if (head1.data < head2.data): head1 = head1.next
        elif (head1.data > head2.data): head2 = head2.next
        else:
            if (prev != None):
                if (prev.data != head1.data):
                    prev.next = Node(head1.data) ; prev = prev.next
            else:
                prev = Node(head1.data) ; head = prev
            head1 = head1.next ; head2 = head2.next
    return head
