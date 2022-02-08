def _create_bit_map ():
    bit_set = [0 for i in range(256)] ; bit_set[0] = 0
    for i in range(256):
        bit_set[i] = (i & 1) + bit_set[i // 2]
    return bit_set

class Solution:
    __bit_set_256 = _create_bit_map()

    def countSetBits (self, n):
        count = 0
        while (n > 0):
            count += Solution.__bit_set_256[n & 255]
            n >>= 8
        return count

    def  sortBySetBitCount (self, arr, n):
        arr.sort(key=lambda x : -self.countSetBits(x))
