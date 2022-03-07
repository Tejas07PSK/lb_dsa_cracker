class ListNode:
    def __init__ (self, data):
        self.data, self.next, self.prev = data, None, None

class Solution:
    def __formSortedDll (self, arr, n):
        arr.sort() ; before, head = None, None
        for i in range(n):
            if (i == 0):
                before = ListNode(arr[i]) ; head = before
            else:
                before.next = ListNode(arr[i]) ; before.next.prev = before
                before = before.next
        return head, before

    def __printTriplets (self, head, tail, k):
        if ((head == None) or (head == tail) or (head.next == tail)):
            print(None) ; print("Count of triplets having sum as {} is {}".format(k, 0)) ; return
        ptr = head ; count = 0
        while (ptr.next != tail):
            i, j = ptr.next, tail
            while ((i != j) and (j.next != i)):
                sum = ptr.data + i.data + j.data
                if (sum < k): i = i.next
                elif (sum > k): j = j.prev
                else:
                    count += 1 ; print((ptr.data, i.data, j.data)) ; i = i.next
            ptr = ptr.next
        print("Count of triplets having sum as {} is {}".format(k, count))

    def __printList (self, head):
        while (head != None):
            print(head.data, end=' ') ; head = head.next
        print()

    def __printListReverse (self, tail):
        while (tail != None):
            print(tail.data, end=' ') ; tail = tail.prev
        print()

    def main (self):
        arr = [2, 5, 4, 9, 8, 1, 6] ; n = len(arr) ; k = 15
        head, tail = self.__formSortedDll(arr, n)
        self.__printList(head) ; self.__printListReverse(tail)
        self.__printTriplets(head, tail, k)

Solution().main()
