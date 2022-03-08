class ListNode:
    def __init__ (self, data):
        self.data, self.next, self.prev = data, None, None

class Solution:
    def __formDll (self, arr, n):
        before, head = None, None
        for i in range(n):
            if (i == 0):
                before = ListNode(arr[i]) ; head = before
            else:
                before.next = ListNode(arr[i]) ; before.next.prev = before
                before = before.next
        return head, before

    def __rotateDLL (self, head, tail, p):
        if (p == 0): return head, tail
        start, end, k = head, head, 1
        while ((k + 1) <= p):
            end, k = end.next, k + 1
        if (end == tail): return head, tail
        head = end.next ; end.next = None
        head.prev = None ; tail.next = start
        start.prev = tail ; tail = end
        return head, tail

    def __printList (self, head):
        while (head != None):
            print(head.data, end=' ') ; head = head.next
        print()

    def __printListReverse (self, tail):
        while (tail != None):
            print(tail.data, end=' ') ; tail = tail.prev
        print()

    def main (self):
        arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] ; n = len(arr) ; p = 4
        head, tail = self.__formDll(arr, n)
        self.__printList(head) ; self.__printListReverse(tail)
        head, tail = self.__rotateDLL(head, tail, p)
        self.__printList(head) ; self.__printListReverse(tail)

Solution().main()
