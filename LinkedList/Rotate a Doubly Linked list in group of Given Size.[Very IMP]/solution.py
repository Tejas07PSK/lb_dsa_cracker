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

    def __printList (self, head):
        while (head != None):
            print(head.data, end=' ') ; head = head.next
        print()

    def __printListReverse (self, tail):
        while (tail != None):
            print(tail.data, end=' ') ; tail = tail.prev
        print()

    def __revDllInGrpOfK (self, head, k):
        prev_end, end = None, head
        start = head ; cnt = 0
        while (start.next != None):
            start.next, start.prev = start.prev, start.next
            start = start.prev ; cnt += 1
            if (cnt == k):
                if (prev_end != None):
                    prev_end.next = start.prev
                else: head = start.prev
                start.prev.prev = prev_end
                prev_end = end ; end.next = None
                end = start ; cnt = 0
        start.next, start.prev = start.prev, start.next
        if (prev_end != None):
            prev_end.next = start
        else: head = start
        start.prev = prev_end
        end.next = None
        return head, end

    def main (self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8] ; n = len(arr) ; k = 4
        head, tail = self.__formDll(arr, n)
        self.__printList(head) ; self.__printListReverse(tail)
        head, tail = self.__revDllInGrpOfK(head, k)
        self.__printList(head) ; self.__printListReverse(tail)

Solution().main()
