'''
class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
'''

class Solution:
    def segregate (self, head):
        ptr = head
        head0, tail0 = None, None
        head1, tail1 = None, None
        head2 = None
        while (ptr != None):
            temp = ptr ; ptr = ptr.next
            if (temp.data == 0):
                temp.next = head0 ; head0 = temp
                if (tail0 == None): tail0 = head0
            elif (temp.data == 1):
                temp.next = head1 ; head1 = temp
                if (tail1 == None): tail1 = head1
            else:
                temp.next = head2 ; head2 = temp
        if (tail0 != None): tail0.next = head1 if (head1 != None) else head2
        if (tail1 != None): tail1.next = head2
        if (head0 != None): head = head0
        elif (head1 != None): head = head1
        else: head = head2
        return head
