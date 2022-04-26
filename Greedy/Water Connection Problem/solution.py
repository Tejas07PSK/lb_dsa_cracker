class Solution:
    def solve (self, n, p, a, b, d):
        in_deg, out_deg, dia = [0 for i in range(n + 1)], [0 for i in range(n + 1)], [0 for i in range(n + 1)]
        for i in range(p): out_deg[a[i]], in_deg[b[i]], dia[a[i]] = b[i], a[i], d[i]
        res = []
        for i in range(1, n + 1):
            if ((in_deg[i] == 0) and (out_deg[i] != 0)):
                temp = [i, out_deg[i], dia[i]]
                while (out_deg[temp[1]] != 0): temp[2], temp[1] = min(temp[2], dia[temp[1]]), out_deg[temp[1]]
                res.append(temp)
        return res
