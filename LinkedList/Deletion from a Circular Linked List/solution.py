class ListNode:
    def __init__ (self, data):
        self.data = data
        self.next = None

class Solution:
    def __formCircularLL (self, arr, n):
        prev, head = None, None
        for i in range(n):
            if (i == 0):
                head = ListNode(arr[i]) ; prev = head
            else:
                prev.next = ListNode(arr[i]) ; prev = prev.next
        prev.next = head
        return head
    
    def __printList (self, head):
        if (head == None):
            print(None) ; return 
        curr = head
        while (curr.next != head):
            print(curr.data, end=" ") ; curr = curr.next
        print(curr.data, end=" ") ; print()

    def __deleteFromCircularLL (self, head, pos):
        if (head.next == head):
            head.next = None
            return None
        curr, prev_tail, tail, size = head, None, None, 0
        while (curr.next != head):
            size += 1 ; prev_tail = curr ; curr = curr.next
        size += 1 ; tail = curr
        if (pos == 1):
            tail.next = head.next ; head.next = None ; head = tail.next
            return head
        if (pos == size):
            prev_tail.next = head ; tail.next = None ; tail = prev_tail
            return head
        prev, curr, i = tail, head, 1
        while (i != pos):
            prev = curr ; curr = curr.next ; i += 1
        prev.next = curr.next ; curr.next = None
        return head

    def main (self):
        arr = [1,2,3,4,5,6] ; n = len(arr)
        print(arr)
        head = self.__formCircularLL(arr, n)
        head = self.__deleteFromCircularLL(head, 4)
        self.__printList(head)

Solution().main()
