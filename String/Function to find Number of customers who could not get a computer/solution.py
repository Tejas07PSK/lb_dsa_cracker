class Solution:
    def runCustomerSimulation (self, nc, cas):
        map = {}
        result, num_of_cus_left = 0, 0
        i = 0
        while (i < len(cas)):
            if (cas[i] not in map):
                map[cas[i]] = 0
            if (map[cas[i]] == 0):
                map[cas[i]] += 1
                if (nc > 0):
                    nc -= 1
                else:
                    num_of_cus_left += 1
                    result += 1
            else:
                map[cas[i]] -= 1
                if (num_of_cus_left > 0):
                    num_of_cus_left -= 1
                else:
                    nc += 1 
            i += 1
        return result
