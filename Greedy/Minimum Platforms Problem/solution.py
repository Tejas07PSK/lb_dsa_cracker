from heapq import heappush, heappop
class Solution:
    def minimumPlatform (self, n, arr, dep):
        trains, min_heap = [(arr[i], dep[i]) for i in range(n)], []
        trains.sort(key=lambda x: x[0]) ; heappush(min_heap, trains[0][1])
        for i in range(1, n):
            if (trains[i][0] > min_heap[0]):
                heappop(min_heap) ; heappush(min_heap, trains[i][1])
            else:
                heappush(min_heap, trains[i][1])
        return len(min_heap)
