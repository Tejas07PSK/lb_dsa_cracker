from queue import PriorityQueue

class ListNode:
    def __init__ (self, data):
        self.data, self.next, self.prev = data, None, None
    def __lt__ (self, other):
        return (self.data < other.data)

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

    def __kSort (self, head, k):
        if ((head == None) or (head.next == None)): return head, head
        before, ptr = None, head ; count = -1
        q = PriorityQueue()
        while (ptr != None):
            if (count <= k):
                before = ptr ; ptr = ptr.next
                before.next, before.prev = None, None
                q.put((before.data, before)) ; before = None ; count += 1
            else:
                temp = (q.get())[1]
                if (before == None):
                    head = temp
                else:
                    before.next = temp ; temp.prev = before
                before = temp ; temp = ptr ; ptr = ptr.next
                temp.next, temp.prev = None, None
                q.put((temp.data, temp))
        while (not q.empty()):
            temp = (q.get())[1]
            before.next = temp ; temp.prev = before
            before = temp
        return head, before

    def __printList (self, head):
        while (head != None):
            print(head.data, end=' ') ; head = head.next
        print()

    def __printListReverse (self, tail):
        while (tail != None):
            print(tail.data, end=' ') ; tail = tail.prev
        print()

    def main (self):
        arr = [10, 9, 8, 7, 4, 70, 60, 50] ; n = len(arr) ; k = 4
        head, tail = self.__formDll(arr, n)
        self.__printList(head) ; self.__printListReverse(tail)
        head, tail = self.__kSort(head, k)
        self.__printList(head) ; self.__printListReverse(tail)

Solution().main()
