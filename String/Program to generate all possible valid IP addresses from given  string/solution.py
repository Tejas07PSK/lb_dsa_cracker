class Solution:
    def getIps (self, string, string_length, string_idx, ip_parts, result, parts_formed_so_far):
        if ((parts_formed_so_far == 4) and (string_idx == string_length)):
            result.append(".".join(ip_parts))
            return
        elif ((parts_formed_so_far == 4) or (string_idx == string_length)):
            return
        i = 1
        while ((i <= 3) and ((string_idx + i) <= string_length)):
            temp_segment = string[string_idx:(string_idx + i)]
            if ((int(temp_segment) > 255) or ((len(temp_segment) > 1) and (temp_segment[0] == '0'))):
                break
            ip_parts[parts_formed_so_far] = temp_segment
            self.getIps(string, string_length, (string_idx + i), ip_parts, result, (parts_formed_so_far + 1))
            ip_parts[parts_formed_so_far] = ""
            i += 1

    def restoreIpAddresses(self, s: str) -> List[str]:
        res, n = [], len(s)
        if ((n < 4) or (n > 12)):
            return res
        parts = ["" for i in range(4)]
        self.getIps(s, n, 0, parts, res, 0)
        return res
