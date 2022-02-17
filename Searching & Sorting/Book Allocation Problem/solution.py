class Solution:
    def validatePossibleAns(self, A, N, M, MID):
        i, part_sum, cntr = 0, 0, 0
        while (i < N):
            if (A[i] > MID):
                return False
            if ((part_sum + A[i]) > MID):
                cntr += 1 ; part_sum = A[i]
                if (cntr >= M):
                    return False
            else: part_sum += A[i]
            i += 1
        return True
            
    def findPages (self, A, N, M):
        right = sum(A) ; ans = right ; left = 1
        while (left <= right):
            mid = left + ((right - left) // 2)
            if self.validatePossibleAns(A, N, M, mid):
                right = mid - 1 ; ans = mid
            else: left = mid + 1
        return ans
