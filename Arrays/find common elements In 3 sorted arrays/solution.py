class Solution:

    def __jumpToLastDuplicate (self, itr, end, lst):
        while ((itr < (end - 1)) and (lst[itr] == lst[itr + 1])):
            itr += 1
        return itr

    def commonElements (self, A, B, C, n1, n2, n3):
        i, j, k = 0, 0, 0
        res = []
        i = self.__jumpToLastDuplicate(i, n1, A)
        j = self.__jumpToLastDuplicate(j, n2, B)
        k = self.__jumpToLastDuplicate(k, n3, C)
        while ((i < n1) and (j < n2) and (k < n3)):
            if (A[i] < B[j]):
                i += 1
                i = self.__jumpToLastDuplicate(i, n1, A)
            elif (A[i] > B[j]):
                j += 1
                j = self.__jumpToLastDuplicate(j, n2, B)
            else:
                if (C[k] < B[j]):
                    k += 1
                    k = self.__jumpToLastDuplicate(k, n3, C)
                elif (C[k] > B[j]):
                    i += 1
                    j += 1
                    i = self.__jumpToLastDuplicate(i, n1, A)
                    j = self.__jumpToLastDuplicate(j, n2, B)
                else:
                    res.append(C[k])
                    i += 1
                    j += 1
                    k += 1
                    i = self.__jumpToLastDuplicate(i, n1, A)
                    j = self.__jumpToLastDuplicate(j, n2, B)
                    k = self.__jumpToLastDuplicate(k, n3, C)
        return res
