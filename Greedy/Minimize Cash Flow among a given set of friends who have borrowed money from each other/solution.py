from collections import defaultdict
from math import inf
def dfs_backtrack (k, balance_list):
    while ((k < len(balance_list)) and (balance_list[k] == 0)): k += 1
    if (k >= len(balance_list)): return 0
    min_trans = inf
    for i in range(k + 1, len(balance_list)):
        if ((balance_list[k] * balance_list[i]) < 0):
            balance_list[i] += balance_list[k]
            min_trans = min(min_trans, 1 + dfs_backtrack(k + 1, balance_list))
            if (balance_list[i] == 0): break
            balance_list[i] -= balance_list[k]
    return min_trans

def settleDebt (arr):
    person_acc_map = defaultdict(int)
    for from, to, amt in arr: person_acc_map[from], person_acc_map[to] = person_acc_map[from] - amt, person_acc_map[to] + amt
    balance_list = person_acc_map.values()
    return dfs_backtrack(0, balance_list)
