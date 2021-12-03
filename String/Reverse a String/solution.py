class Solution:
    def __swap (self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def reverseString(self, s: List[str]) -> None:
        i, j = 0, len(s) - 1
        while (i < j):
            self.__swap(s, i, j)
            i += 1
            j -= 1
