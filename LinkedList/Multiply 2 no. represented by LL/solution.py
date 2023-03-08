class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
    def __del__ (self):
        if(self.next): del self.next

def reverse (head):
    prev, curr = None, head
    while (curr):
        tmp = curr.next
        curr.next = prev
        prev, curr = curr, tmp
    return prev

def multiplyLL (head1, head2):
    head1, head2 = reverse(head1), reverse(head2)
    ptr2, new_head = head2, None
    prev_ptr, new_ptr = None, None
    while (ptr2):
        ptr1 = head1
        ptr = new_ptr
        carry = 0
        while (ptr1):
            if (ptr == None):
                ptr = Node(0)
                if (prev_ptr != None): prev_ptr.next = ptr
            dig_prd = (ptr1.data * ptr2.data) + ptr.data + carry
            ptr.data = dig_prd % 10
            carry = dig_prd // 10
            if (new_head == None): new_head, new_ptr = ptr, ptr
            prev_ptr = ptr
            ptr, ptr1 = ptr.next, ptr1.next
        while(carry > 0):
            if (not ptr):
                ptr = Node(0)
                if (prev_ptr != None): prev_ptr.next = ptr
            sm = ptr.data + carry
            ptr.data = sm % 10
            carry = sm // 10
            prev_ptr = ptr
            ptr = ptr.next
        prev_ptr = new_ptr
        new_ptr = new_ptr.next
        ptr2 = ptr2.next
    new_head = reverse(new_head)
    while ((new_head.data == 0) and (new_head.next != None)):
        tmp = new_head
        new_head = new_head.next
        del tmp
    return new_head
