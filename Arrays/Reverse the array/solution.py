def reverseWord (s):
    chr_lst = list(s)
    for i in range(len(s) // 2): chr_lst[i], chr_lst[len(s) - i - 1] = chr_lst[len(s) - i - 1], chr_lst[i]
    return "".join(chr_lst)
