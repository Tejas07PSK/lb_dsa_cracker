class Solution:
    def store_freq_in_hm (self, s, hm):
        for c in s:
            if c in hm:
                hm[c] += 1
            else:
                hm[c] = 1

    def checkIfGivenStrigIsAShuffleOfTowOther (self, s1, s2, s3):
        hm = {}
        self.store_freq_in_hm(s2, hm)
        self.store_freq_in_hm(s3, hm)
        for c in s1:
            if ((c in hm) and (hm[c] != 0)):
                hm[c] -= 1
            else:
                return False
        return True
