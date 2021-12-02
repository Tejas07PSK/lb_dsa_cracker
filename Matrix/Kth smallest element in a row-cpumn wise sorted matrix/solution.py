import math

class MinHeap:
    def __init__ (self, row_idx, arr, N):
        self.__heap_arr = []
        i = 0
        while (i < N):
            self.__heap_arr.append({
                "element": arr[i],
                "row": row_idx,
                "column": i
            })
            i += 1
        self.__last_idx = N - 1

    def __swap(self, i, j):
        temp = self.__heap_arr[i]
        self.__heap_arr[i] = self.__heap_arr[j]
        self.__heap_arr[j] = temp

    def delete (self):
        res = self.__heap_arr[0]
        self.__heap_arr[0] = self.__heap_arr[self.__last_idx]
        i = 0
        while (i < self.__last_idx):
            left, right = ((2 * i) + 1), ((2 * i) + 2)
            left_ele = self.__heap_arr[left]["element"] if (left < self.__last_idx) else math.inf
            right_ele = self.__heap_arr[right]["element"] if (right < self.__last_idx) else math.inf
            if ((left >= self.__last_idx) and (right >= self.__last_idx)) or ((self.__heap_arr[i]["element"] <= left_ele) and (self.__heap_arr[i]["element"] <= right_ele)):
                break
            if (left_ele <= right_ele):
                self.__swap(i, left)
                i = left
            else:
                self.__swap(i, right)
                i = right
        return res

    def insert (self, obj):
        self.__heap_arr[self.__last_idx] = obj
        i = self.__last_idx
        while ((i > 0) and (self.__heap_arr[i]["element"] < self.__heap_arr[(i - 1) // 2]["element"])):
            self.__swap(i, ((i - 1) // 2))
            i = (i - 1) // 2

def kthSmallest (mat, N, K):
    mh = MinHeap(0, mat[0], N)
    op = {}
    i = 0
    while (i < K):
        op = mh.delete()
        mh.insert({
            "element": mat[op["row"] + 1][op["column"]] if ((op["row"] + 1) < N) else math.inf,
            "row": op["row"] + 1,
            "column": op["column"]
        })
        i += 1
    return op["element"]
