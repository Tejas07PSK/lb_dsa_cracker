from collections import defaultdict
from math import inf
def dfs_backtrack (k, balance_list, dp_hm):
    while ((k < len(balance_list)) and (balance_list[k] == 0)): k += 1
    if (k >= len(balance_list)): return 0
    #if (k in dp_hm): return dp_hm[k]   ----> use this only if question asks for greedy solution
    min_trans = inf
    for i in range(k + 1, len(balance_list)):
        if ((balance_list[k] * balance_list[i]) < 0):
            balance_list[i] += balance_list[k]
            min_trans = min(min_trans, 1 + dfs_backtrack(k + 1, balance_list, dp_hm))
            #if (balance_list[i] == 0): break   ----> use this only if question asks for greedy solution
            balance_list[i] -= balance_list[k]
    min_trans = 0 if (min_trans == inf) else min_trans
    #dp_hm[k] = min_trans   ----> use this only if question asks for greedy solution
    return min_trans

def settleDebt (arr):
    person_acc_map, dp_hm = defaultdict(int), {}
    for send, rcv, amt in arr:
        person_acc_map[send] -= amt ; person_acc_map[rcv] += amt
    balance_list = [val for val in person_acc_map.values() if val != 0]
    #print(balance_list)
    return dfs_backtrack(0, balance_list, dp_hm)
