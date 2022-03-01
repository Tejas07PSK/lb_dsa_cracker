'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''

class Solution:
    def merge (self, head1, head2):
        head, prev, curr1, curr2 = None, None, head1, head2
        while ((curr1 != None) and (curr2 != None)):
            if (curr1.data <= curr2.data):
                if (prev == None): head = curr1
                else: prev.next = curr1
                prev = curr1 ; curr1 = curr1.next
            else:
                if (prev == None): head = curr2
                else: prev.next = curr2
                prev = curr2 ; curr2 = curr2.next
        if (curr2 != None): prev.next = curr2
        if (curr1 != None): prev.next = curr1
        return head

    def mergeSort (self, head):
        if (head.next == None):
            return head
        if ((head.next != None) and (head.next.next == None)):
            if (head.next.data < head.data):
                temp = head.next ; temp.next = head
                head.next = None ; head = temp
            return head
        slow_ptr, fast_ptr = head, head
        while ((fast_ptr.next != None) and (fast_ptr.next.next != None)):
            slow_ptr = slow_ptr.next ; fast_ptr = fast_ptr.next.next
        head2 = slow_ptr.next ; slow_ptr.next = None
        head1 = self.mergeSort(head) ; head2 = self.mergeSort(head2)
        return self.merge(head1, head2)
