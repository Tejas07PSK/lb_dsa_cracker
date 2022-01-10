class Solution:
    def secFrequent (self, arr, N):
        map = {}
        for string in arr:
            if (string not in map):
                map[string] = 1
            else:
                map[string] += 1
        high_count, high_string, sec_high_count, sec_high_string = 0, "", 0, ""
        for string, freq in map.items():
            if (freq > high_count):
                sec_high_count = high_count
                sec_high_string = high_string
                high_count = freq
                high_string = string
            elif ((freq < high_count) and (freq > sec_high_count)):
                sec_high_count = freq
                sec_high_string = string
        return sec_high_string
